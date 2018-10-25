from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    
    register_blueprint(app)

    with app.app_context():
        pass
    return app


def register_blueprint(app):
    from app.web.main import web
    app.register_blueprint(web)