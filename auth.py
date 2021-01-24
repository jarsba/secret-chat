from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash
from werkzeug.security import safe_str_cmp
from models.user import User

db = SQLAlchemy()

def authenticate(username, password):
    user = db.session.query(User).filter(User.username == username).one()
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    user = db.session.query(User).filter(User.id == user_id).one()
    return user
