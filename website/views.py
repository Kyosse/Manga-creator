from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


"""
INFO A RETENIR
mettre @login_required entre @views.route(...) et def ...
pour empecher d'accèder à la page sans être connecté

"""

@views.route('/')
def home():
    

    return render_template("home.html", user=current_user)



@views.route("/scan")
def scan():
    
    return render_template("scan.html", user=current_user)