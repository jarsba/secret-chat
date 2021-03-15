from auth import authenticate, identity
import os
from threading import Lock
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from dotenv import load_dotenv
from flask_jwt import JWT
from flask_bcrypt import Bcrypt
from datetime import timedelta

from routes import api, Session

import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

# APP

app = Flask(__name__, static_folder='build', static_url_path='')
CORS(app)
async_mode = None
# Routes registered from sockets.py
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")

app.register_blueprint(api)

app.debug = os.getenv('FLASK_ENV') != 'production'

# DB

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SQLALCHEMY_ECHO'] = True

db_url = os.getenv('SC_DB_URL')
db_port = os.getenv('SC_DB_PORT')
db_name = os.getenv('SC_DB_NAME')
db_user = os.getenv('SC_DB_USER')
db_password = os.getenv('SC_DB_PASSWORD')

db_connection_url = f"postgres://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}"

app.config['SQLALCHEMY_DATABASE_URI'] = db_connection_url

# JWT

app.config["SECRET_KEY"] = os.getenv("SC_SECRET_KEY")
app.config["JWT_AUTH_URL_RULE"] = "/api/login"
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=21600)
bcrypt = Bcrypt(app)

jwt = JWT(app, authenticate, identity)

# MIDDLEWARE

@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.remove()


if __name__ == '__main__':
    load_dotenv()
    debug = os.getenv('FLASK_ENV') != 'production'
    port = os.getenv('SC_FLASK_PORT')
    socketio.run(app, host='0.0.0.0', port=port, debug=debug)
