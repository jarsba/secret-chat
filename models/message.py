from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates="messages")
    content = db.Column(db.String)
    room_id = db.Column(db.Integer, db.ForeignKey('chat_room.id'),
                     nullable=False)
    room = db.relationship('ChatRoom', back_populates="messages")

    def __repr__(self):
        return f'<Message {self.id}>'
