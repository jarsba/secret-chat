from auth import authenticate, identity
import os
from flask import Flask, url_for, jsonify
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
from flask_jwt import JWT, jwt_required, current_identity
from flask_bcrypt import generate_password_hash

from flask_bcrypt import Bcrypt
import auth
from models.user import User
from models.chat_room import ChatRoom
from models.message import Message

import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

# APP

app = Flask(__name__)
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

db = SQLAlchemy(app)

# JWT

app.config["SC_SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_AUTH_URL_RULE"] = "/login"

bcrypt = Bcrypt(app)

jwt = JWT(app, authenticate, identity)

app.wsgi_app = DispatcherMiddleware(
    Response('Not Found', status=404),
    {'/api': app.wsgi_app}
)


def render_response(data="", status_code=200, message=""):
    return jsonify({
        'data': data,
        'status_code': status_code,
        'message': message
    })



@app.route("/user", methods=['GET'])
def get_all_users():
    users = db.session.query(User).all()
    return render_response(data=users)

@app.route("/user/<id>", methods=['GET'])
def get_user(id):
    user = db.session.query(User).filter(User.id == id).one()
    return render_response(data=user)


@app.route("/user", methods=['POST'])
def create_user():
    request_data = request.get_json()

    email = request_data['email']
    username = request_data['username']
    password = request_data['password']

    new_user = User(email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return render_response(data=new_user)


@app.route("/user/<id>", methods=['DELETE'])
def delete_user(id):
    user = db.session.query(User).filter(User.id == id).one()
    db.session.delete(user)
    db.session.commit()

    return render_response()


@app.route("/user/<id>", methods=['PUT'])
def update_user(id):
    request_data = request.get_json()

    email = request_data['email']
    username = request_data['username']
    password = request_data['password']

    user = db.session.query(User).filter(User.id == id).one()

    if email:
        user.email = email
    if username:
        user.username = username
    if password:
        user.password = generate_password_hash(
            password, os.getenv('SC_BCRYPT_LOG_ROUNDS')
        ).decode()

    db.session.add(user)
    db.session.commit()

    return render_response(data=user)


@app.route("/secret")
@jwt_required()
def secret():
    return render_response("Secret!")


if __name__ == '__main__':
    load_dotenv()
    debug = os.getenv('FLASK_ENV') != 'production'
    port = os.getenv('SC_FLASK_PORT')
    app.run('0.0.0.0', port, debug=debug)
