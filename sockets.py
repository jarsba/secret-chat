from flask import jsonify, Blueprint
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import logging

from main import socketio

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)


@socketio.event
def my_event(message):
    logger.info(message)
    emit('my_response',
         {'data': message['data'],})


@socketio.event
def my_broadcast_event(message):
    logger.info(message)
    emit('my_response',
         {'data': message['data'],},
         broadcast=True)


@socketio.event
def join(message):
    logger.info(message)
    join_room(message['room'])
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),})


@socketio.event
def leave(message):
    logger.info(message)
    leave_room(message['room'])
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms())})


@socketio.on('close_room')
def on_close_room(message):
    logger.info(message)
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',},
         to=message['room'])
    close_room(message['room'])


@socketio.event
def my_room_event(message):
    logger.info(message)
    emit('my_response',
         {'data': message['data'], },
         to=message['room'])


@socketio.event
def disconnect_request():
    logger.info("Disconnect")
    def can_disconnect():
        disconnect()

    # for this emit we use a callback function
    # when the callback function is invoked we know that the message has been
    # received and it is safe to disconnect
    emit('my_response',
         {'data': 'Disconnected!',},
         callback=can_disconnect)


@socketio.event
def my_ping():
    emit('my_pong')


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count})

@socketio.event
def connect():
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on("message")
def on_message():
    emit('my_response', {'data': 'Connected', 'count': 0})



@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


