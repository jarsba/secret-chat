from main import db

from models.user import User
from models.message import Message
from models.chat_room import ChatRoom

import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info(f'Starting DB seeding')
logger.info(f'Creating database and tables')

db.create_all()

logger.info(f'Creating users')

admin = User(email='admin@secretchat.com', username='admin', password='')
user1 = User(email='admin@secretchat.com', username='user1', password='')
user2 = User(email='admin@secretchat.com', username='user2', password='')

db.session.add(admin)
db.session.add(user1)
db.session.add(user2)
db.session.commit()

logger.info(f'Creating chat rooms')

room1 = ChatRoom(name='topic1')
room2 = ChatRoom(name='topic2')
room3 = ChatRoom(name='topic3')

db.session.add(room1)
db.session.add(room2)
db.session.add(room3)
db.session.commit()

logger.info(f'Creating messages')

message1 = Message(user=admin.id, content='admin message', room=room1.id)
message2 = Message(user=user1.id, content='user1 message', room=room1.id)
message3 = Message(user=user2.id, content='user2 message', room=room2.id)

db.session.add(message1)
db.session.add(message2)
db.session.add(message3)
db.session.commit()
