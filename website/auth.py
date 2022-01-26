from flask import Flask, request, Blueprint, render_template, flash, redirect, url_for
from .models import User, Manga
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # Définition du chemin d'accès (URL, METHODE(GET,POST)) méthode étant les différents envoies d'infos
def login():
    
    return render_template("login.html", user=current_user) # On renvoie à la page de login en cas d'érreur

@auth.route('/logout') # URL pour se déconnecter
@login_required # On précise que cette URL n'est accessible seulement si tu es connecté
def logout():
    logout_user() # Fonction de déconnection du module de login
    return redirect(url_for('auth.login')) # On redirige vers la page de connection

@auth.route('/sign-up', methods=['GET', 'POST']) # Définition du chemin d'accès (URL, METHODE(GET,POST)) méthode étant les différents envoies d'infos
def sign_up():
    
    return render_template("sign_up.html", user=current_user) # Sinon redirection vers la page d'incription