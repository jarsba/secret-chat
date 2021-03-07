from auth import authenticate, identity
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from flask import Flask, url_for, jsonify, Blueprint
from flask import redirect, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.wrappers import Response
from flask_jwt import JWT, jwt_required, current_identity
from flask_bcrypt import generate_password_hash
from flask_bcrypt import Bcrypt
from datetime import timedelta

from models import User
from models import ChatRoom
from models import Message

import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

# CONSTANT

PATH_PREFIX = '/api'

# APP

app = Flask(__name__, static_folder='../build', static_url_path='/')

CORS(app)
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

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername="postgresql",
        host=db_url,
        port=db_port,
        username=db_user,
        password=db_password,
        database=db_name,
    ),
)

Session = sessionmaker(bind=db)

# JWT

app.config["SECRET_KEY"] = os.getenv("SC_SECRET_KEY")
app.config["JWT_AUTH_URL_RULE"] = "/api/login"
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=21600)
bcrypt = Bcrypt(app)

jwt = JWT(app, authenticate, identity)


def render_response(data="", status_code=200, message=""):
    return jsonify({
        'data': data,
        'status_code': status_code,
        'message': message
    })


print(app.url_map)


# For React
@app.route('/<a>')
def index(a):
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route(f"{PATH_PREFIX}/user", methods=['GET'])
@jwt_required()
def get_all_users():
    logger.info("Get all users")
    session = Session()
    users = session.query(User).all()
    return render_response(data=users)


@app.route(f"{PATH_PREFIX}/user/<id>", methods=['GET'])
@jwt_required()
def get_user(id):
    logger.info("Get a user")
    session = Session()
    user = session.query(User).filter(User.id == id).one()
    return render_response(data=user)


@app.route(f"{PATH_PREFIX}/user", methods=['POST'])
@jwt_required()
def create_user():
    logger.info("Create a user")
    session = Session()

    request_data = request.get_json()

    email = request_data['email']
    username = request_data['username']
    password = request_data['password']

    new_user = User(email=email, username=username, password=password)
    session.add(new_user)
    session.commit()
    return render_response(data=new_user)


@app.route(f"{PATH_PREFIX}/user/<id>", methods=['DELETE'])
@jwt_required()
def delete_user(id):
    logger.info("Delete a user")
    session = Session()

    user = session.query(User).filter(User.id == id).one()
    session.delete(user)
    session.commit()

    return render_response()


@app.route(f"{PATH_PREFIX}/user/<id>", methods=['PUT'])
@jwt_required()
def update_user(id):
    logger.info("Update a user")
    session = Session()

    request_data = request.get_json()

    email = request_data['email']
    username = request_data['username']
    password = request_data['password']

    user = session.query(User).filter(User.id == id).one()

    if email:
        user.email = email
    if username:
        user.username = username
    if password:
        user.password = generate_password_hash(
            password, os.getenv('SC_BCRYPT_LOG_ROUNDS')
        ).decode()

    session.add(user)
    session.commit()

    return render_response(data=user)


@app.route(f"{PATH_PREFIX}/chatroom", methods=['GET'])
@jwt_required()
def get_all_chatrooms():
    logger.info("Get all chatrooms")
    session = Session()
    chatrooms = session.query(ChatRoom).all()
    return render_response(data=chatrooms)


@app.route(f"{PATH_PREFIX}/chatroom/<id>", methods=['GET'])
@jwt_required()
def get_chatroom(id):
    logger.info("Get a chatroom")
    session = Session()
    chatroom = session.query(ChatRoom).filter(ChatRoom.id == id).one()
    return render_response(data=chatroom)


@app.route(f"{PATH_PREFIX}/chatroom", methods=['POST'])
@jwt_required()
def create_chatroom():
    logger.info("Create a chatroom")
    session = Session()
    request_data = request.get_json()
    name = request_data['name']
    new_room = ChatRoom(name=name)
    session.add(new_room)
    session.commit()
    return render_response(data=new_room)


@app.route(f"{PATH_PREFIX}/chatroom/<id>", methods=['DELETE'])
@jwt_required()
def delete_room(id):
    logger.info("Delete a chatroom")
    session = Session()

    chatroom = session.query(ChatRoom).filter(ChatRoom.id == id).one()
    session.delete(chatroom)
    session.commit()

    return render_response()


@app.route(f"{PATH_PREFIX}/message", methods=['GET'])
@jwt_required()
def get_all_messages():
    logger.info("Get all messages")
    session = Session()
    messages = session.query(Message).all()
    return render_response(data=messages)


@app.route(f"{PATH_PREFIX}/message/chatroom/<id>", methods=['GET'])
@jwt_required(id)
def get_all_messages_from_chatroom(id):
    logger.info("Get all messages from specific chatroom")
    session = Session()
    messages = session.query(Message).filter(ChatRoom.id == id).all()
    return render_response(data=messages)


@app.route(f"{PATH_PREFIX}/message/user/<id>", methods=['GET'])
@jwt_required(id)
def get_all_messages_from_user(id):
    logger.info("Get all messages from specific user")
    session = Session()
    messages = session.query(Message).filter(User.id == id).all()
    return render_response(data=messages)


@app.route(f"{PATH_PREFIX}/message/<id>", methods=['GET'])
@jwt_required()
def get_message(id):
    logger.info("Get a message")
    session = Session()
    message = session.query(Message).filter(Message.id == id).one()
    return render_response(data=message)


@app.route(f"{PATH_PREFIX}/message", methods=['POST'])
@jwt_required()
def create_message():
    logger.info("Create a message")
    session = Session()

    request_data = request.get_json()

    user_id = request_data['user_id']
    content = request_data['content']
    room_id = request_data['room_id']
    recipient_id = request_data['recipient_id']

    new_message = Message(user_id=user_id, content=content, room_id=room_id, recipient_id=recipient_id)
    session.add(new_message)
    session.commit()
    return render_response(data=new_message)


@app.route(f"{PATH_PREFIX}/secret")
@jwt_required()
def secret():
    return render_response("Secret!")


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


if __name__ == '__main__':
    load_dotenv()
    debug = os.getenv('FLASK_ENV') != 'production'
    port = os.getenv('SC_FLASK_PORT')
    print(app.url_map)
    app.run('0.0.0.0', port, debug=debug)
