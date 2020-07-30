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


SERIAL_PORT = "/dev/ttyUSB0"
SERIAL_BAUD = 115200

ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=0)
HOST = '0.0.0.0'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
while True:
    try:
        conn, addr = s.accept()
        t1 = threading.Thread(target=readSerialWriteToSocket, args=(ser, conn,))
        t1.daemon = True
        t1.start()
        readSocketWriteToSerial(ser, conn)
    except ConnectionResetError:
        conn.close()
    except EOFError:
        conn.close()
    except KeyboardInterrupt:
        break
    except serial.serialutil.SerialException:
        ser.close()
        ser.open()
s.close()
s.detach()
