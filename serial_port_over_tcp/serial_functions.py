import config as config
from socket_functions import *


def readSerialWriteToSocket(serial_connection, socket_connection):
    while True:
        data = None
        if config.OPTIMIZE_FOR_SERIAL_LINES:
            data = serial_connection.readline()
        else:
            data = serial_connection.read()
        # data = pickle.dumps(data)
        socket_connection.sendall(data)


def readSocketWriteToSerial(serial_connection, socket_connection):
    while True:
        data = recvall(socket_connection)
        # data = pickle.loads(data)
        serial_connection.write(data)
