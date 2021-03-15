from flask import Flask, url_for, jsonify, Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity
from flask_bcrypt import generate_password_hash
from flask_cors import CORS
import sqlalchemy
from sqlalchemy import or_, and_
from sqlalchemy.orm import sessionmaker, scoped_session, load_only
import logging
import os
from dotenv import load_dotenv
from datetime import timezone, datetime
from models import User
from models import ChatRoom
from models import Message

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)
load_dotenv()

api = Blueprint('api', __name__, url_prefix="/api")
CORS(api)

# DB

db_url = os.getenv('SC_DB_URL')
db_port = os.getenv('SC_DB_PORT')
db_name = os.getenv('SC_DB_NAME')
db_user = os.getenv('SC_DB_USER')
db_password = os.getenv('SC_DB_PASSWORD')

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername="postgresql",
        host=db_url,
        port=db_port,
        username=db_user,
        password=db_password,
        database=db_name,
    ),
    pool_size=30,
    max_overflow=0
)

Session = scoped_session(sessionmaker(bind=db, autocommit=False, autoflush=False))


def render_response(data="", status_code=200, message=""):
    return jsonify({
        'data': data,
        'status_code': status_code,
        'message': message
    })


### ROUTES ###


# For React
@api.route('/')
def index():
    return api.send_static_file('index.html')


@api.route(f"user", methods=['GET'])
@jwt_required()
def get_all_users():
    logger.info("Get all users")
    session = Session()
    users = session.query(User.id, User.created_at, User.updated_at, User.email, User.username).all()
    print(users)
    return render_response(data=users)


@api.route(f"user/<id>", methods=['GET'])
@jwt_required()
def get_user(id):
    logger.info("Get a user")
    session = Session()
    user = session.query(User).filter(User.id == id).one()
    return render_response(data=user)


@api.route(f"user", methods=['POST'])
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


@api.route(f"user/<id>", methods=['DELETE'])
@jwt_required()
def delete_user(id):
    logger.info("Delete a user")
    session = Session()

    user = session.query(User).filter(User.id == id).one()
    session.delete(user)
    session.commit()
    return render_response()


@api.route(f"user/<id>", methods=['PUT'])
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


@api.route(f"chatroom", methods=['GET'])
@jwt_required()
def get_all_chatrooms():
    logger.info("Get all chatrooms")
    session = Session()
    chatrooms = session.query(ChatRoom).all()
    return render_response(data=chatrooms)


@api.route(f"chatroom/<id>", methods=['GET'])
@jwt_required()
def get_chatroom(id):
    logger.info("Get a chatroom")
    session = Session()
    chatroom = session.query(ChatRoom).filter(ChatRoom.id == id).one()
    return render_response(data=chatroom)


@api.route(f"chatroom", methods=['POST'])
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


@api.route(f"chatroom/<id>", methods=['DELETE'])
@jwt_required()
def delete_room():
    logger.info("Delete a chatroom")
    session = Session()

    chatroom = session.query(ChatRoom).filter(ChatRoom.id == id).one()
    session.delete(chatroom)
    session.commit()

    return render_response()


@api.route(f"message", methods=['GET'])
@jwt_required()
def get_all_messages():
    logger.info("Get all messages")
    session = Session()
    messages = session.query(Message).all()
    return render_response(data=messages)


@api.route(f"message/chatroom/<id>", methods=['GET'])
@jwt_required()
def get_all_messages_from_chatroom(id):
    logger.info("Get all messages from specific chatroom")
    session = Session()
    messages = session.query(Message).filter(Message.room_id == id).all()
    return render_response(data=messages)


@api.route(f"message/user/<id>", methods=['GET'])
@jwt_required()
def get_all_messages_with_user(id):
    logger.info("Get all messages from conversation with specific user")
    user_id = current_identity.id
    session = Session()
    messages = session.query(Message).filter(or_(and_(Message.recipient_id == id, Message.user_id == user_id),
                                                 and_(Message.recipient_id == user_id, Message.user_id == id))).all()
    return render_response(data=messages)


@api.route(f"message/<id>", methods=['GET'])
@jwt_required()
def get_message(id):
    logger.info("Get a message")
    session = Session()
    message = session.query(Message).filter(Message.id == id).one()
    return render_response(data=message)


@api.route(f"message", methods=['POST'])
@jwt_required()
def create_message():
    logger.info("Create a message")
    session = Session()

    request_data = request.get_json()

    user_id = current_identity.id
    content = request_data['content']
    room_id = request_data['room_id'] if 'room_id' in request_data else None
    recipient_id = request_data['recipient_id'] if 'recipient_id' in request_data else None

    new_message = Message(created_at=datetime.now(timezone.utc), updated_at=datetime.now(timezone.utc), user_id=user_id,
                          content=content, room_id=room_id, recipient_id=recipient_id)
    session.add(new_message)
    session.commit()
    return render_response(data=new_message)


@api.route(f"message/<id>", methods=['DELETE'])
@jwt_required()
def delete_message(id):
    logger.info("Delete a message")
    session = Session()

    message = session.query(Message).filter(Message.id == id).one()
    session.delete(message)
    session.commit()

    return render_response()


@api.route(f"secret")
@jwt_required()
def secret():
    return render_response("Secret!")


@api.route('/<path:path>')
def static_file(path):
    return api.send_static_file(path)


@api.errorhandler(404)
def not_found(e):
    return api.send_static_file('index.html')
