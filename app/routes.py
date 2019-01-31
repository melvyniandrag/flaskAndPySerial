from flask import render_template
from flask import jsonify
from app import app
import collections
import serial
import threading
import time
import struct

#ser = serial.Serial("/dev/ttyACM0", 9600)
N = 5
d = collections.deque([ 0 for i in range(N) ], maxlen=N)

def f():
    global d
    ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    while True:
        try:
            data = struct.unpack('>h', b'\x00' + ser.read())[0]
            d.append(data)
        except Exception as e:
            print(str(e))

threading.Thread(target=f).start()

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