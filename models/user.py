from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash
import os

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    messages = db.relationship('Message', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(
            password, os.getenv('SC_BCRYPT_LOG_ROUNDS')
        ).decode()

    def __repr__(self):
        return f'<User {self.username}>'
