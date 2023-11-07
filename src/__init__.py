from flask import Flask


def main() -> None:
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello world"

    return app
