import pickle
import socket
import threading

import serial


def recvall(sock, n=4096):
    data = bytearray()
    while True:
        packet = sock.recv(n)
        if not packet:  # Important!!
            break
        data.extend(packet)
        if len(packet) < n:
            break
    return data


def readSerialWriteToSocket(serial_connection, socket_connection):
    while True:
        try:
            data = serial_connection.readline()
            data = pickle.dumps(data)
            socket_connection.sendall(data)
        except KeyboardInterrupt:
            return
        except serial.serialutil.SerialException:
            return
        except ConnectionResetError:
            return
        except EOFError:
            return
        except KeyboardInterrupt:
            break


def readSocketWriteToSerial(serial_connection, socket_connection):
    while True:
        data = recvall(socket_connection)
        data = pickle.loads(data)
        serial_connection.write(data)


SERIAL_PORT = "/dev/ttyUSB1"
SERIAL_BAUD = 115200
ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 8080))

while True:
    try:
        t1 = threading.Thread(target=readSerialWriteToSocket, args=(ser, conn,))
        t1.daemon = True
        t1.start()
        readSocketWriteToSerial(ser, conn)
    except ConnectionResetError:
        conn.connect(('localhost', 8080))
    except EOFError:
        conn.close()
    except KeyboardInterrupt:
        break
    except serial.serialutil.SerialException:
        try:
            ser.close()
            ser.open()
            continue
        except serial.serialutil.SerialException:
            continue
    except OSError:
        print("Server has shut down")
        break
