import cv2
import pickle
import socket
import time

HOST = '0.0.0.0'
PORT = 8011

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)

cam = cv2.VideoCapture(1)
cam.set(3, 1280)
cam.set(4, 720)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]

conn, addr = s.accept()

while True:
    ret, frameOriginal = cam.read()
    result, frame = cv2.imencode('.jpg', frameOriginal, encode_param)
    data = pickle.dumps(frame)
    conn.sendall(data)
