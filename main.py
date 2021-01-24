from auth import authenticate, identity
import os
from flask import Flask, url_for, jsonify
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
from flask_jwt import JWT, jwt_required, current_identity
from flask_bcrypt import Bcrypt
import auth
import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

# APP

app = Flask(__name__)
app.debug = os.getenv('FLASK_ENV') != 'production'

# DB

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SC_DB_URL"] = os.getenv('SC_DB_URL')
db = SQLAlchemy(app)

# JWT

app.config["SC_SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_AUTH_URL_RULE"] = "/login"

bcrypt = Bcrypt(app)

jwt = JWT(app, authenticate, identity)

app.wsgi_app = DispatcherMiddleware(
    Response('Not Found', status=404),
    {'/api': app.wsgi_app}
)


def render_response(data, status_code=200, message=""):
    return jsonify({
        'data': data,
        'status_code': status_code,
        'message': message
    })


@app.route("/")
def index():
    return render_response("Heipparallaa!")


@app.route("/secret")
@jwt_required()
def secret():
    return render_response("Secret!")


if __name__ == '__main__':
    load_dotenv()
    debug = os.getenv('FLASK_ENV') != 'production'
    app.run('0.0.0.0', 5000, debug=debug)
