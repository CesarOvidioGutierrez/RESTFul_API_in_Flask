import logging
from constants import EMAIL_AND_PASSWORD_ERROR_MESSAGE

class ValidationEmailError(Exception):
    pass


def validate_email_and_password(request):
    email = request.json.get('email')
    password = request.json.get('password')
    if not email or not password:
        logging.error(EMAIL_AND_PASSWORD_ERROR_MESSAGE)
        raise ValidationEmailError(EMAIL_AND_PASSWORD_ERROR_MESSAGE)
