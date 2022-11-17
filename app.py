from flask import Flask, request,render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS
from models import setup_db, db, Users
from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# db = SQLAlchemy()

# migrate = Migrate(app, db)


def create_app():
 
    app = Flask(__name__)
  
    setup_db(app)

  
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))


    from auth import auth as auth_blueprint;
    app.register_blueprint(auth_blueprint)


    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app





