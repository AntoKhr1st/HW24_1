from flask import Flask

from lesson23_project_source.views import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app

