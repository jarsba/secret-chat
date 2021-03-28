from flask import jsonify, Blueprint
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect, Namespace
import logging

from main import socketio

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

@socketio.event
def join(message):
    logger.info("JOINING ROOM")
    logger.info(message)
    join_room(message['room'])
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()), })

@socketio.event
def leave(message):
    logger.info("LEAVING ROOM")
    logger.info(message)
    leave_room(message['room'])
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms())})

@socketio.on('close_room')
def on_close_room(message):
    logger.info("CLOSING ROOM")
    logger.info(message)
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.', },
         to=message['room'])
    close_room(message['room'])

@socketio.event
def my_room_event(message):
    logger.info(message)
    emit('my_response',
         {'data': message['data'], },
         to=message['room'])

@socketio.event
def my_ping():
    print("PONG")
    emit('my_pong')


@socketio.event
def connect():
    print("CONNECTED")
    emit('my_response', {'data': 'Connected', 'count': 0})

@socketio.on("message")
def on_message():
    print("MESSAGE RECEIVED")
    emit('my_response', {'data': 'Connected', 'count': 0})
