from flask import Flask, request, Blueprint, render_template, flash, redirect, url_for
from .models import User, Manga
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # Définition du chemin d'accès (URL, METHODE(GET,POST)) méthode étant les différents envoies d'infos
def login():
    """[Fonction permettant de gérer les tentatives de connection pour les utilisateurs]

    Returns:
        [Redirection vers home.html]: [Renvoie vers la page home si la connection est validé]
        [Redirection vers login.html]: [Renvoie vers la page login si la connection échoue car non valide]
    """
    if request.method == 'POST': # Condition pour traiter seulement si l'utilisateur envoie une demande de connection et non à chaque fois qu'il recharge la page
        username = request.form.get('username').lower() # Récupération des infos envoyés par l'utilisateur dans le form
        motdepasse = request.form.get('password') # lower de l'username car ça permet de ne pas avoir à traiter les problèmes de majuscules sur les identifaints

        # Recherche dans la base de données si il esxiste bien un username comme celui dans le form
        user = User.query.filter_by(identifiant=username, statut='actif').first()

        if user: # si il y en a un alors 
            if check_password_hash(user.motdepasse, motdepasse): # On vérifie si les 2 mdp coïncident
                flash('Logged in successfully !', category='success') # Ils coïncident donc on envoie un message de succès
                login_user(user, remember=True) # Puis on dit au module, qui gère les login user, qu'il est connecté et qu'il doit s'en souvenir dans la cache du navigateur
                return redirect(url_for('views.home')) # Puis on renvoie sur la page d'acceuil
            else: # Sinon on affiche un message d'érreur
                flash('Incorrect password or username, try again', category='error')
        else: # Sinon on affiche un message d'érreur
            flash('Username does not exist', category='error')
    return render_template("login.html", user=current_user) # On renvoie à la page de login en cas d'érreur

@auth.route('/logout') # URL pour se déconnecter
@login_required # On précise que cette URL n'est accessible seulement si tu es connecté
def logout():
    logout_user() # Fonction de déconnection du module de login
    return redirect(url_for('auth.login')) # On redirige vers la page de connection

@auth.route('/sign-up', methods=['GET', 'POST']) # Définition du chemin d'accès (URL, METHODE(GET,POST)) méthode étant les différents envoies d'infos
def sign_up():
    """[Fonction permettant de gérer les inscriptions des nouveaux utilisateurs]

    Returns:
        [Redirection vers home.html]: [Renvoie vers la page home si la connection est validé]
        [Redirection vers sign-up.html]: [Renvoie vers la page d'incription si la connection échoue car non valide]
    """
    if request.method == 'POST': # Condition pour traiter seulement si l'utilisateur envoie une demande de connection et non à chaque fois qu'il recharge la page
        username = request.form.get('username').lower() # Récupération des infos envoyés par l'utilisateur dans le form
        password1 = request.form.get('password1') # lower de l'username car ça permet de ne pas avoir à traiter les problèmes de majuscules sur les identifaints
        password2 = request.form.get('password2')
        pseudo = request.form.get('username')
        
        # Recherche dans la base de données si il esxiste un username comme celui dans le form
        user = User.query.filter_by(identifiant=username).first() 
        if user: # Si oui alors on renvoie un message pour dire qu'il est déjà pris
            flash('Username already exists', category='error')
        elif len(username) <= 4 or '.' in password1 or len(password1) > 16:
            flash('Username need to have between 4 and 15 caracters, not having . ', category='error')
        elif len(password1) <= 8 or '.' in password1 or len(password1) > 16:
            flash('Password need to have between 8 and 15 caracters, not having . ', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        else: # Si toutes les valeurs sont valides alors on ajoute celle-ci à la base de données
            new_user = User(identifiant=username,
                            motdepasse=generate_password_hash(password1, method='sha256'),
                            statut='actif',
                            pseudo=pseudo) #statut valeur de compte(actif)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True) # Puis on dit au module, qui gère les login user, qu'il est connecté et qu'il doit s'en souvenir dans la cache du navigateur
            flash('Account created !', category='success') # Message de confiramtion de création
            return redirect(url_for('views.home')) # Redirection vers la page d'acceuil
    
    return render_template("sign_up.html", user=current_user) # Sinon redirection vers la page d'incription


@auth.route('/profile', methods=['GET','POST']) # Définition du chemin d'accès (URL, METHODE(GET,POST)) méthode étant les différents envoies d'infos
@login_required # On précise que cette URL n'est accessible seulement si tu es connecté
def profile():
    """[Fonction pour enregistrer les mangas ajoutés par l'utilisateur ét modifier ses paramètres profile]

    Returns:
        [Redirection]: [redirige vers la page profile.html]
    """
    # En cours
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        for file in request.files.getlist('images'):
            print(file.filename)
    return render_template('profile.html', user=current_user)