import pickle
import socket

HOST = 'localhost'
PORT = 8011

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)

msg = []
for i in range(0, 10000000):
    msg.append("Hello!")

msg = pickle.dumps(msg)

conn, addr = s.accept()
conn.sendall(msg)
conn.close()
s.close()
s.detach()
