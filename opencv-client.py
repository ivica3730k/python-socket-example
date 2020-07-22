import cv2
import pickle
import socket
import numpy as np


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


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8011))

while True:
    try:
        data = recvall(client_socket)
        data = np.array(data)
        img = cv2.imdecode(data, cv2.IMREAD_COLOR)
        cv2.imshow('Pic', img)
        cv2.waitKey(1)
    except:
        print("Error")
