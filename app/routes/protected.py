"""/protected - 
este endpoint deberá estar protegido y sólo ser accesible mediante el uso del token de acceso proporcionado en el endpoint /login."""

from flask import Blueprint, jsonify
from app.middlewares import token_required
from app.middlewares import ValidationTokenError

protected_blueprint = Blueprint('protected_blueprint', __name__)

@protected_blueprint.route('/protected', methods=['GET', 'POST'])
@token_required
def protected_user(current_user):
    return jsonify({'message': '¡Hola mundo desde protected!'})
    
