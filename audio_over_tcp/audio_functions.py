import threading

import Fifo
import config

_received_queue = Fifo.Fifo()
silence = chr(0) * config.CHUNK * 2 * 2

_sending_queue = Fifo.Fifo()


def receive_audio(audio_stream, socket_connection, chunk=config.CHUNK):
    t1 = threading.Thread(target=play_audio, args=(audio_stream,))
    t1.start()
    while True:
        _received_queue.put(socket_connection.recv(chunk))


def send_audio(audio_stream, socket_connection, chunk=config.CHUNK):
    t1 = threading.Thread(target=record_audio, args=(audio_stream,))
    t1.start()
    while True:
        if len(_sending_queue):
            socket_connection.sendall(_sending_queue.get(chunk))


def play_audio(audio_stream, chunk=config.CHUNK):
    while True:
        if len(_received_queue):
            audio_stream.write(bytes(_received_queue.get(chunk)))
        else:
            audio_stream.write(silence)


def record_audio(audio_stream, chunk=config.CHUNK):
    while True:
        _sending_queue.put(bytes(audio_stream.read(chunk, exception_on_overflow=False)))