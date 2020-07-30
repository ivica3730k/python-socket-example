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
        data = serial_connection.read()
        # data = pickle.dumps(data)
        socket_connection.sendall(data)


def readSocketWriteToSerial(serial_connection, socket_connection):
    while True:
        data = recvall(socket_connection)
        # data = pickle.loads(data)
        serial_connection.write(data)
