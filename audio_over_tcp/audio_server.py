import socket
import threading

import pyaudio

import audio_functions
import config

HOST = '0.0.0.0'  # This means our server can be accessed from everywhere
PORT = config.PORT

CHUNK = config.CHUNK
FORMAT = pyaudio.paInt16
MONO = 1
RATE = config.RATE
AUDIO = pyaudio.PyAudio()
AUDI0_INPUT_STREAM = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, input=True, frames_per_buffer=CHUNK)
AUDIO_OUTPUT_STREAM = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, output=True, frames_per_buffer=CHUNK)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    t1 = threading.Thread(target=audio_functions.receive_audio, args=(AUDIO_OUTPUT_STREAM, conn,))
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=audio_functions.send_audio, args=(AUDI0_INPUT_STREAM, conn,))
    t2.daemon = True
    t2.start()

s.close()
s.detach()
