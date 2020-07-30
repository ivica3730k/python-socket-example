import socket
import threading

import serial

import serial_functions

SERIAL_PORT = "/dev/ttyUSB0"
SERIAL_BAUD = 9600
ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)

HOST = '0.0.0.0'
PORT = 8080

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

"""    except ConnectionResetError:
        conn.close()
    except EOFError:
        conn.close()"""
