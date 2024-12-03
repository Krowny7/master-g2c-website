from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, News, Application, Event, Teacher, Ranking
from forms import ApplicationForm, LoginForm, ContactForm
from admin import init_admin
import os
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///master_g2c.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Initialize admin
admin = init_admin(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Blueprints
public = Blueprint('public', __name__)
auth = Blueprint('auth', __name__, url_prefix='/auth')

# Auth routes
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin.index'))
        return redirect(url_for('public.index'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            if user.is_admin:
                return redirect(url_for('admin.index'))
            return redirect(url_for('public.index'))
        flash('Invalid email or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.accueil'))

# Public routes
@public.route('/')
def accueil():
    return render_template('public/accueil.html')

@public.route('/formations')
def formations():
    formations = {
        'licence': [
            {'nom': 'Informatique', 'duree': '3 ans', 'description': 'Formation en sciences informatiques'},
            {'nom': 'Mathématiques', 'duree': '3 ans', 'description': 'Formation en mathématiques fondamentales et appliquées'},
            {'nom': 'Physique', 'duree': '3 ans', 'description': 'Formation en sciences physiques'}
        ],
        'master': [
            {'nom': 'Intelligence Artificielle', 'duree': '2 ans', 'description': 'Spécialisation en IA et Machine Learning'},
            {'nom': 'Cybersécurité', 'duree': '2 ans', 'description': 'Formation en sécurité informatique'},
            {'nom': 'Data Science', 'duree': '2 ans', 'description': 'Analyse de données et Big Data'}
        ]
    }
    return render_template('public/formations.html', formations=formations)

@public.route('/recherche')
def recherche():
    laboratoires = [
        {
            'nom': 'LABO-IA',
            'domaine': 'Intelligence Artificielle',
            'description': 'Recherche en apprentissage automatique et robotique',
            'projets': ['Robotique cognitive', 'Deep Learning', 'Vision par ordinateur']
        },
        {
            'nom': 'LABO-CYBER',
            'domaine': 'Cybersécurité',
            'description': 'Sécurité des systèmes d\'information',
            'projets': ['Cryptographie', 'Sécurité réseau', 'Blockchain']
        }
    ]
    return render_template('public/recherche.html', laboratoires=laboratoires)

@public.route('/vie_etudiante')
def vie_etudiante():
    # Récupérer les événements depuis la base de données
    events = Event.query.order_by(Event.date.desc()).all()
    
    associations = [
        {
            'nom': 'BDE',
            'description': 'Bureau des Étudiants',
            'activites': ['Soirées', 'Événements culturels', 'Integration']
        },
        {
            'nom': 'Club Robotique',
            'description': 'Association de robotique',
            'activites': ['Projets robots', 'Compétitions', 'Workshops']
        }
    ]
    return render_template('public/vie_etudiante.html', associations=associations, events=events)

@public.route('/contact')
def contact():
    return render_template('public/contact.html')

@public.route('/admissions')
def admissions():
    return render_template('public/admissions.html')

@public.route('/debouches')
def debouches():
    return render_template('public/debouches.html')

@public.route('/equipe')
def equipe():
    teachers = Teacher.query.order_by(Teacher.order).all()
    return render_template('public/equipe.html', teachers=teachers)

@public.route('/pourquoi_g2c')
def pourquoi_g2c():
    ranking = Ranking.query.order_by(Ranking.year.desc()).first()
    return render_template('public/pourquoi_g2c.html', ranking=ranking)

@public.route('/temoignages')
def temoignages():
    return render_template('public/temoignages.html')

# Register blueprints
app.register_blueprint(public, url_prefix='')
app.register_blueprint(auth, url_prefix='/auth')

@app.cli.command("init-ranking")
def init_ranking():
    """Initialize ranking data."""
    ranking = Ranking(
        position=2,
        year=2024,
        category="Masters Gestion des Risques Financiers & Conformité",
        category_en="Masters in Financial Risk Management & Compliance",
        source="Meilleurs Masters",
        url="https://meilleurs-masters.com/master-gestion-des-risques-financiers-compliance-conformite/iae-caen-master-gestion-d-actifs-controle-des-risques-et-conformite.html"
    )
    db.session.add(ranking)
    db.session.commit()
    print("Ranking initialized successfully!")

@app.cli.command("create-admin")
def create_admin():
    """Create an admin user."""
    admin = User(
        email="admin@g2c.fr",
        is_admin=True
    )
    admin.password_hash = generate_password_hash("adminG2C2024!")
    db.session.add(admin)
    db.session.commit()
    print("Admin user created successfully!")

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('static/uploads'):
            os.makedirs('static/uploads')
    app.run(host='0.0.0.0', port=5000, debug=True)
