from flask import Blueprint, render_template

public = Blueprint('public', __name__)

@public.route('/')
def accueil():
    return render_template('public/accueil.html')

@public.route('/formations')
def formations():
    return render_template('public/formations.html')

@public.route('/pourquoi-g2c')
def pourquoi_g2c():
    return render_template('public/pourquoi_g2c.html')

@public.route('/equipe')
def equipe():
    return render_template('public/equipe.html')

@public.route('/admissions')
def admissions():
    return render_template('public/admissions.html')

@public.route('/contact')
def contact():
    return render_template('public/contact.html')

@public.route('/chatbox')
def chatbox():
    return render_template('public/chatbox.html')

@public.route('/carrieres')
def carrieres():
    """Page des carrières et débouchés."""
    return render_template('public/carrieres.html')
