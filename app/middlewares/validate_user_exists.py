from app.models.user import User
import logging
from constants import USER_ALREADY_EXISTS_ERROR_MESSAGE

class ValidationUserExistsError(Exception):
    pass

def validate_user_exists(request):
    email = request.json.get('email')
    user = User.find_user_by_email(email=email)
    if user:
        logging.error(USER_ALREADY_EXISTS_ERROR_MESSAGE)
        raise ValidationUserExistsError(USER_ALREADY_EXISTS_ERROR_MESSAGE)