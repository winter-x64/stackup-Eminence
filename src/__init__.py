from flask import Flask


def main() -> None:
    app = Flask(__name__)

    from . import auth

    app.register_blueprint(blueprint=auth, auth="/auth")

    return app
