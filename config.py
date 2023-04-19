import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_jwt_extended import JWTManager
from database import initialize_db
from app.routes import register_blueprint, login_blueprint, protected_blueprint 

def configure_app(app):
    # Configuración de JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Configuración de MongoDB
    app.config['MONGODB_SETTINGS'] = {
        'db': os.getenv('NAME_DATABASE'),
        'host': os.getenv('HOST'),
        'port': int(os.getenv('PORT'))
    }

    # Configuración de logs
    handler = RotatingFileHandler(os.getenv('SECRET_KEY'), maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # Inicialización de la base de datos
    initialize_db(app)

    # Configuración de JWT
    jwt = JWTManager(app)

    # Registra los blueprints
    app.register_blueprint(register_blueprint)  
    app.register_blueprint(login_blueprint)  
    app.register_blueprint(protected_blueprint)  

    return app

def configure_logging():
    logging.basicConfig(filename=os.getenv('NAME_LOG'), level=logging.ERROR)