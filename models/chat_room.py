from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ChatRoom(db.Model):
    __tablename__ = 'chat_room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    messages = db.relationship('Message', backref='room', lazy=True)

    def __repr__(self):
        return f'<Room {self.name}>'
