from flask import render_template
from flask import jsonify
from app import app
import collections
import serial
import threading

#ser = serial.Serial("/dev/ttyACM0", 9600)
N = 5
d = collections.deque([ 0 for i in range(N) ], maxlen=N)

@app.route("/")
@app.route("/index")
def index():
    about = { "subject": "Flask & PySerial" }
    return render_template( 'index.html', title="Sample Project", about=about )

@app.route("/getNewData", methods = ["GET",])
def get_new_data():
    global N, d
    indices = list(range(N))
    # put some random stuff here for testing AJAX
    data = dict(zip(indices, list(d)))
    return jsonify( data )