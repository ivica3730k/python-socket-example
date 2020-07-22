import cv2
import numpy as np
import pickle
import socket


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


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8011))

while True:
    try:
        frame = recvall(client_socket)
        frame = np.array(frame)
        img = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        cv2.imshow('Pic', img)
        cv2.waitKey(1)
    except pickle.UnpicklingError:
        continue
    except cv2.error:
        continue
