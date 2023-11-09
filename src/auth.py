from flask import Blueprint, render_template

auth = Blueprint(name="auth", import_name=__name__)


@auth.route("/login", methods=["GET", "POST"])
def login(request):
    if request.method == "POST":
        pass
    return render_template("login.html")


@auth.route("/logout")
def logout(request):
    user = ""
    return render_template("login.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup(request):
    if request.method == "POST":
        pass
    user = ""
    return render_template("login.html")
