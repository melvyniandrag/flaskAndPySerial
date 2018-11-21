import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
    data = ser.readline().rstrip()
    intData = int(data)
    print(intData)
