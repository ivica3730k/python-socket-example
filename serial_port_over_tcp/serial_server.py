import socket
import threading

import serial

import config as config
import serial_functions

SERIAL_PORT = config.Server.SERIAL_PORT
ser = serial.Serial(SERIAL_PORT, timeout=1)

HOST = '0.0.0.0'  # This means our server can be accessed from everywhere
PORT = config.PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    t1 = threading.Thread(target=serial_functions.readSerialWriteToSocket, args=(ser, conn,))
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=serial_functions.readSocketWriteToSerial, args=(ser, conn,))
    t2.daemon = True
    t2.start()

s.close()
s.detach()
