import os
from flask import Blueprint, request, jsonify
from app.middlewares import populate_user, validate_password
from app.middlewares import ValidationPasswordError

login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.before_request
@populate_user
def before():
    try:
        validate_password(request)
    except ValidationPasswordError as e:
        return jsonify({'message': str(e)}), 401

@login_blueprint.route('/login', methods=['POST'])
def login_user():
    secret_key = os.getenv('SECRET_KEY').encode('utf-8')
    user = request.json.get('user')

    #TODO: Sacar 'super-secret' en un env

    token = user.generate_token(secret_key)

    return jsonify({'token': token})


"""/login - 
este endpoint permitirá a los usuarios autenticarse proporcionando su nombre de email y contraseña. 
Si la autenticación es exitosa, deberá devolver un token de acceso que será necesario para acceder a los endpoints protegidos.
"""
