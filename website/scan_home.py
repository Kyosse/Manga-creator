from . import db
from .models import Manga
from flask import Flask, request, Blueprint, render_template, flash, redirect, url_for
from sqlalchemy import select

from flask_login import current_user

"""
FONCTION DE TEST BROUILLON

"""

def cinq():
    # Fonctions temp pour ajouter des manga factice dans la database
    for i in range(5):
        new_manga = Manga(auteur='test', seen_value=i, user_id=current_user.id)

        db.session.add(new_manga)
        db.session.commit()


def update_popular():
    """Fonction qui affiche les manga suivants les catégories affichés sur la page home

    Returns:
        [list]: popular= une liste des cinqs manga les plus populaires suivants la base de données
    """ 
    popular = []

    # Commande pour inserer des mangass factice pour les test
    cinq()
    
    # Commande pour récupérer les 5 mangas les plus vues
    list_five_pop = Manga.query.order_by(Manga.seen_value.desc()).limit(5).offset(0).all()
    
    for manga in list_five_pop:
        # manga doit être ajouté dans le append pour prendre les valeurs de la base de données
        popular.append({'img': 'logo.png', 'desc':'update'}) # Valeur factice dans le append
        popular.append({'img': 'test_home.png', 'desc':'update'}) # Valeur factice dans le append
    return popular        

