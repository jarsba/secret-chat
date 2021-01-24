from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'),
                     nullable=False)
    content = db.Column(db.String)
    room = db.Column(db.Integer, db.ForeignKey('chat_room.id'),
                     nullable=False)

    def __repr__(self):
        return f'<Message {self.id}>'
