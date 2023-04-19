from constants import SPLIT_NAME_ERROR_MESSAGE, NAME_REQUIRED_ERROR_MESSAGE
import logging

class ValidationSplitNameError(Exception):
    pass

def split_name(request):
    name = request.json.get('name')
    if name:
        first_name, last_name = name.split(',')
        if not first_name or not last_name:
            logging.error(SPLIT_NAME_ERROR_MESSAGE)
            raise ValidationSplitNameError(SPLIT_NAME_ERROR_MESSAGE)
        request.json['first_name'] = first_name.strip()
        request.json['last_name'] = last_name.strip()
    else:
        logging.error(NAME_REQUIRED_ERROR_MESSAGE)
        raise ValidationSplitNameError(NAME_REQUIRED_ERROR_MESSAGE)
        