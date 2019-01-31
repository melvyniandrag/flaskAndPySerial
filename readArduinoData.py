import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
    time.sleep(0.1)
    data = ser.readline().rstrip()
    intData = int(data)
    print(intData)
