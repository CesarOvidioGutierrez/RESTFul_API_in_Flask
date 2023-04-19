import os
from flask import Blueprint, request, jsonify

from app.models.user import User
from app.middlewares import split_name, validate_email_and_password, validate_user_exists
from app.middlewares import ValidationSplitNameError, ValidationEmailError, ValidationUserExistsError

# TODO: Ver mejorar  agregar satusCode http,  carteleria, destructuring en register_user. Por ultimo preguntar en chat que mejorar.

register_blueprint = Blueprint('register_blueprint', __name__)

@register_blueprint.before_request
def before():
    try:
        split_name(request)
        validate_email_and_password(request)
        validate_user_exists(request)
    except ValidationSplitNameError as e:
        return jsonify({'message': str(e)}), 400
    except ValidationEmailError as e:
        return jsonify({'message': str(e)}), 400
    except ValidationUserExistsError as e:
        return jsonify({'message': str(e)}), 409
    

@register_blueprint.route('/register', methods=['POST'])
def register_user():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)

    # Create and save user
    user = User.create_user(email=email, password=password, first_name=first_name, last_name=last_name)

    #TODO: Sacar 'super-secret' en un env
    token = user.generate_token(str(os.getenv('SECRET_KEY')))
    
    return jsonify({'token': token})



""" /register - 
este endpoint permitirá a los usuarios registrarse proporcionando su nombre de usuario y contraseña.
 La contraseña deberá ser encriptada antes de ser almacenada en la base de datos. 
 """
