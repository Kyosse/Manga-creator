from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialisation de la base de données
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():