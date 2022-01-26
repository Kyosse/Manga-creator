from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Manga(db.Model):
    id_manga = db.Column(db.Integer, primary_key=True) # id
    auteur = db.Column(db.String(50)) # Auteur du manga
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Date posté sur le site
    seen_value = db.Column(db.Integer) # Valeur de popularité
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Lien avec User pour savoir qui l'a posté


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # id SQL 
    identifiant = db.Column(db.String(16), unique=True) # Identifiant de connection
    motdepasse = db.Column(db.String(16)) # mdp
    statut = db.Column(db.String(16)) # Statut ( compte activé ou désactivé/suppr) 'actif' ou 'inactif'
    pseudo = db.Column(db.String(16), unique=True) # Pseudo entré lors de la création du compte et qui sera affiché 
    mangas = db.relationship('Manga') # Relation avec la classe manga pour savoir qui à posté

