from flask_bcrypt import generate_password_hash, check_password_hash
from werkzeug.security import safe_str_cmp
from models import User
import logging
import main
logger = logging.getLogger(__name__)


def authenticate(username, password):
    session = main.Session()
    user = session.query(User).filter(User.username == username).one()
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    logger.info(payload)
    session = main.Session()
    user_id = payload['identity']
    user = session.query(User).filter(User.id == user_id).one()
    return user
