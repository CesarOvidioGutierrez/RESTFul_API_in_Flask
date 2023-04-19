import logging
from constants import PASSWORD_ERROR_MESSAGE, CREDENTIALS_ERROR_MESSAGE

class ValidationPasswordError(Exception):
    pass

def validate_password(request):
    password = request.json.get('password')
    if not password:
        logging.error(PASSWORD_ERROR_MESSAGE)
        raise ValidationPasswordError(PASSWORD_ERROR_MESSAGE)
    
    user = request.json.get('user')
    if not user.check_password(password):
        logging.error(CREDENTIALS_ERROR_MESSAGE)
        raise ValidationPasswordError(CREDENTIALS_ERROR_MESSAGE)