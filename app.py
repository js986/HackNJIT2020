from os.path import dirname, join
import os
import json
import flask
import flask_socketio
import flask_sqlalchemy
from dotenv import load_dotenv
import ffmpeg

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

database_uri = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app


db.create_all()
db.session.commit()

import models 

@socketio.on("new user")
def on_new_user(data):
    db.session.add(models.AppUser("tonytiger@gmail.com","Tony","Tiger", models.AuthUserType.GOOGLE,"tonytiger.png"))
    


@app.route('/')
def index():
    models.db.create_all()
    return flask.render_template("index.html")
    
@app.route('/login')
def login():
    return flask.render_template("login.html")
    
if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )