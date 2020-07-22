import pickle
import socket

import cv2

HOST = '0.0.0.0'
PORT = 8011

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost', 8011))

cam = cv2.VideoCapture(1)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    frame = pickle.dumps(frame)
    socket.sendall(frame)
