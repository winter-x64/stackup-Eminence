from flask import Flask


def main():
    # app config
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "this is key"

    # import all Blueprints
    from . import auth
    from .views.home import home

    # register all blueprints
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(auth.auth, url_prefix="/auth")

    return app
