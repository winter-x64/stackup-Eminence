from flask import Blueprint, render_template

from ..models import events

home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"])
def index():
    return render_template("home/home.html")


@home.route("/lister", methods=["GET", "POST"])
def events():
    event = events.query.all()
    return render_template("home/home.html", event=event)
