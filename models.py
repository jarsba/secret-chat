import os
from datetime import datetime, timezone
from flask_bcrypt import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

Base = declarative_base()


@dataclass
class ChatRoom(Base):
    __tablename__ = 'chat_room'
    id: int = Column(Integer, primary_key=True)
    created_at: datetime = Column(
        DateTime,
        nullable=True,
        default=datetime.now(timezone.utc),
    )
    updated_at: datetime = Column(
        DateTime,
        nullable=True,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    name: str = Column(String)
    messages = relationship('Message', back_populates='room')


@dataclass
class Message(Base):
    __tablename__ = 'message'
    id: int = Column(Integer, primary_key=True)
    created_at: datetime = Column(
        DateTime,
        nullable=True,
        default=datetime.now(timezone.utc),
    )
    updated_at: datetime = Column(
        DateTime,
        nullable=True,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    user_id: int = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates="messages", foreign_keys=[user_id])
    content: str = Column(String)
    room_id: int = Column(Integer, ForeignKey('chat_room.id'),
                          nullable=True)
    room = relationship('ChatRoom', back_populates="messages")
    recipient_id: int = Column(Integer, ForeignKey('user.id'),
                               nullable=True)
    recipient = relationship('User', foreign_keys=[recipient_id])

    def __init__(self, user_id, content, room_id, recipient_id, created_at=datetime.now(timezone.utc),
                 updated_at=datetime.now(timezone.utc)):
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_id = user_id
        self.content = content
        self.room_id = room_id
        self.recipient_id = recipient_id


@dataclass
class User(Base):
    __tablename__ = 'user'
    id: int = Column(Integer, primary_key=True)
    created_at: datetime = Column(
        DateTime,
        nullable=True,
        default=datetime.now(timezone.utc),
    )
    updated_at: datetime = Column(
        DateTime,
        nullable=True,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    email: str = Column(String)
    username: str = Column(String)
    password: str = Column(String)
    messages = relationship('Message', back_populates='user', foreign_keys="Message.user_id")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(
            password, int(os.getenv('SC_BCRYPT_LOG_ROUNDS'))
        ).decode()
