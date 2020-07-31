import socket
import threading

import serial

import config as config
import serial_functions

SERIAL_PORT = config.Client.SERIAL_PORT
ser = serial.Serial(SERIAL_PORT, timeout=1)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((config.Client.SERVER_IP, config.PORT))
t1 = threading.Thread(target=serial_functions.readSerialWriteToSocket, args=(ser, conn,))
t1.start()
t2 = threading.Thread(target=serial_functions.readSocketWriteToSerial, args=(ser, conn,))
t2.start()
