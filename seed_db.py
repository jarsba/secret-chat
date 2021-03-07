import os
import logging
from main import db, Session
from models import ChatRoom
from models import User
from models import Message
from sqlalchemy.ext.declarative import declarative_base

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info(f'Starting DB seeding')

logger.info(f'Creating database and tables')

Base = declarative_base()
Base.metadata.create_all(db, tables=[ChatRoom.__table__, User.__table__, Message.__table__])

session = Session()

logger.info(f'Creating chat rooms')

room1 = ChatRoom(name='topic1')
room2 = ChatRoom(name='topic2')
room3 = ChatRoom(name='topic3')

session.add(room1)
session.add(room2)
session.add(room3)
session.commit()

logger.info(f'Creating users')

admin = User(email='admin@secretchat.com', username='admin', password='admin')
user1 = User(email='user1@secretchat.com', username='user1', password='user1')
user2 = User(email='user2@secretchat.com', username='user2', password='user2')

session.add(admin)
session.add(user1)
session.add(user2)
session.commit()


logger.info(f'Creating messages')

message1 = Message(user_id=admin.id, content='admin message', room_id=room1.id)
message2 = Message(user_id=user1.id, content='user1 message', room_id=room1.id)
message3 = Message(user_id=user2.id, content='user2 message', room_id=room2.id)

session.add(message1)
session.add(message2)
session.add(message3)
session.commit()
