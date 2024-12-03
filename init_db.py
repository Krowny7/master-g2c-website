from app import app, db
from models import User
from werkzeug.security import generate_password_hash

def init_db():
    with app.app_context():
        # Drop all tables first
        db.drop_all()
        
        # Create tables
        db.create_all()
        
        # Create admin user
        admin = User(
            email='admin@master-g2c.fr',
            password_hash=generate_password_hash('admin123'),
            is_admin=True  # Make sure is_admin is set to True
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")

if __name__ == '__main__':
    init_db()
