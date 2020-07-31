import socket
import threading

import pyaudio

import audio_functions
import config

CHUNK = config.CHUNK
FORMAT = pyaudio.paInt16
MONO = 1
RATE = config.RATE
AUDIO = pyaudio.PyAudio()
AUDI0_INPUT_STREAM = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, input=True, frames_per_buffer=CHUNK)
AUDIO_OUTPUT_STREAM = AUDIO.open(format=FORMAT, channels=MONO, rate=RATE, output=True, frames_per_buffer=CHUNK)
listening_sock = socket.socket(socket.AF_INET,  # Internet
                               socket.SOCK_DGRAM)  # UDP
listening_sock.bind(("0.0.0.0", config.Server.CLIENT_PORT))
sending_sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP

t1 = threading.Thread(target=audio_functions.receive_audio, args=(AUDIO_OUTPUT_STREAM, listening_sock,))
t1.daemon = False
t1.start()
t2 = threading.Thread(target=audio_functions.send_audio, args=(AUDI0_INPUT_STREAM, sending_sock, "CLIENT",))
t2.daemon = False
t2.start()