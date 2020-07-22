import _thread
import pickle
import socket

import cv2

HOST = '0.0.0.0'
PORT = 8011


def recvall(sock, n=1024):
    data = bytearray()
    while True:
        packet = sock.recv(n)
        if not packet:  # Important!!
            break
        data.extend(packet)
        if len(packet) < n:
            break
    return data


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)


def handle_socket(conn, addr):
    while True:
        try:
            data = recvall(conn)
            data = pickle.loads(data)
            img = cv2.imdecode(data, cv2.IMREAD_COLOR)
            cv2.imshow(str(addr), img)
            cv2.waitKey(1)
        except pickle.UnpicklingError:
            continue
        except:
            break


while True:
    conn, addr = s.accept()
    print("New Client")
    _thread.start_new_thread(handle_socket, (conn, addr))
