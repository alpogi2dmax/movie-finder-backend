from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from extensions import db, bcrypt
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from models import User

# db = SQLAlchemy()
# bcrypt = Bcrypt()

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    db.init_app(app)
    bcrypt.init_app(app)
    api = Api(app)

    from resources.register import RegisterResource
    from resources.login import LoginResource
    from resources.checksession import CheckSessionResource
    from resources.logout import LogoutResource

    api.add_resource(RegisterResource, '/register')
    api.add_resource(LoginResource, '/login')
    api.add_resource(CheckSessionResource, '/checksession')
    api.add_resource(LogoutResource, '/logout')

    return app

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        db.create_all()

    app.run(debug=True)