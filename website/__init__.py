from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialisation de la base de données
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN' # Clé secret global
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Association BDD et Fichier de la BDD
    # Stand by, configuration pour le dl des images
    app.config['UPLOAD_FOLDER'] = 'website/static/images/scan/' 
    app.config['MAX_CONTENT_PATH'] = 20 * 1024 * 1024
    db.init_app(app) # Lancement de la BDD
    
    
    
     # Import du model de la BDD
    from .models import User, Manga

    create_database(app) # Initialisation du modèle de la BDD
    
    return app

def create_database(app):
    """[Créer le fichier de la base de donnée si il n'est pas déjà présent

    Args:
        app :
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        