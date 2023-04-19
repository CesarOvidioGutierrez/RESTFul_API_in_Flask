import jwt
import os
from app.models.user import User
from functools import wraps
from flask import request, jsonify, abort
import logging
from datetime import datetime
from constants import INVALID_TOKEN_ERROR_MESSAGE, TOKEN_EXPIRED_ERROR_MESSAGE, TOKEN_ERROR_MESSAGE

class ValidationTokenError(Exception):
    pass

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            
            token = request.headers.get('Authorization', '').split(' ')[1]
            if not token:
                logging.error(INVALID_TOKEN_ERROR_MESSAGE)
                raise ValidationTokenError(INVALID_TOKEN_ERROR_MESSAGE)
            secret_key = os.getenv('SECRET_KEY').encode('utf-8')
            decoded_data = jwt.decode(token, secret_key, algorithms=["HS256"])
            if decoded_data['exp'] < datetime.utcnow().timestamp():
                logging.error(TOKEN_EXPIRED_ERROR_MESSAGE)
                return ValidationTokenError(TOKEN_EXPIRED_ERROR_MESSAGE)
            current_user = User.find_user_by_id(decoded_data['user_id'])
        except ValidationTokenError as e:
            return jsonify({'message': str(e)}), 401
        except Exception as e:
            logging.error(TOKEN_ERROR_MESSAGE)
            return jsonify({'message': TOKEN_ERROR_MESSAGE }), 500
        return f(current_user, *args, **kwargs)
    return decorated