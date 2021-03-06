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

data = recvall(client_socket)
a = pickle.loads(data)
print(len(a))
