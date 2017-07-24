# views.py

from flask import render_template
from flask_socketio import SocketIO, send
from app import app

socketio = SocketIO(app)
@socketio.on('message')
def handleMessage(msg):
    if msg == 'user_connected':
        send('Hi. I am Spock. An AI. How can I help you?', broadcast=False)
    else:
        send (msg + ' recieved')
        
    

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

