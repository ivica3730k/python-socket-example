import pickle
import socket
import struct

import cv2

cap = cv2.VideoCapture(0)
# cap.set(3,800)
# cap.set(4,600)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost', 8011))
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cap.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(frame)
    socket.sendall(struct.pack("L", len(data)) + data)
