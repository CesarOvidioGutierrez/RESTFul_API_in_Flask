from database import db
from passlib.hash import pbkdf2_sha256 as sha256
import jwt
import datetime

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    first_name = db.StringField(required=True, min_length=6)
    last_name = db.StringField(required=True, min_length=6)

    @classmethod
    def create_user(cls, email, password, first_name, last_name):
        user = cls(email=email, password=sha256.hash(str(password)), first_name=first_name, last_name=last_name)
        user.save()
        return user
    
    def check_password(self, password):
        return sha256.verify(str(password), self.password)
    
    def generate_token(self, secret_key):
        expires_in = datetime.timedelta(days=1)
        token = jwt.encode({'user_id': str(self.id), 'exp': datetime.datetime.utcnow() + expires_in}, secret_key)
        return token
    
    @staticmethod
    def find_user_by_email(email):
        user = User.objects(email=email).first()
        return user
    
    @staticmethod
    def find_user_by_id(id):
        user = User.objects(id=id).first()
        return user