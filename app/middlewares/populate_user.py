import logging
from app.models.user import User
from functools import wraps
from flask import request, jsonify
from constants import USER_NOT_EXIST_ERROR_MESSAGE

class ValidationPopulateUserError(Exception):
    pass

def populate_user(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            email = request.json.get('email')
            user = User.find_user_by_email(email=email)
            if not user:
                logging.error(USER_NOT_EXIST_ERROR_MESSAGE)
                raise ValidationPopulateUserError(USER_NOT_EXIST_ERROR_MESSAGE)
        except ValidationPopulateUserError as e:
            return jsonify({'message': str(e)}), 401
        request.json['user'] = user
    return wrapper