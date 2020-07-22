import cv2
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
        data = recvall(client_socket)
        frame = pickle.loads(data, fix_imports=True, encoding="bytes")
        img = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        cv2.imshow('Pic', img)
        cv2.waitKey(1)
    except pickle.UnpicklingError:
        continue
