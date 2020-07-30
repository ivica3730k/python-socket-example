import socket
import threading

import serial

import serial_functions

SERIAL_PORT = "/dev/ttyUSB1"
SERIAL_BAUD = 9600
ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 8080))
t1 = threading.Thread(target=serial_functions.readSerialWriteToSocket, args=(ser, conn,))
t1.start()
t2 = threading.Thread(target=serial_functions.readSocketWriteToSerial, args=(ser, conn,))
t2.start()
