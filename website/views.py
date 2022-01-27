from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .scan_home import cinq, update_popular

views = Blueprint('views', __name__)


"""
INFO A RETENIR
mettre @login_required entre @views.route(...) et def ...
pour empecher d'accèder à la page sans être connecté

"""

@views.route('/')
def home():
    popular = update_popular()

    return render_template("home.html", user=current_user,popular=popular)



@views.route("/scan")
def scan():
    
    return render_template("scan.html", user=current_user)