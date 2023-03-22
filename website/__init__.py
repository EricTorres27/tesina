from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path



DB_NAME = "aplicacion_tesina"
db = SQLAlchemy()

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY']='hjshshshshshs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/aplicacion_tesina'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Session, Role, UserSession
    
    with app.app_context():
        db.drop_all()
        db.create_all()
    
    return app


    