"""
Configuration file for audio_over_udp program.
This configuration file is for both client and the server, so keep the same file on client and server side.
"""

"""
Configurations for both sides
"""

# Audio parameters, do not exceed chunk greater that 4096
CHUNK = 512
RATE = 44100

"""
Configuration for client side
"""


class Client:
    SERVER_IP = "192.168.1.104"
    SERVER_PORT = 8081


class Server:
    CLIENT_IP = "192.168.1.107"
    CLIENT_PORT = 8082
