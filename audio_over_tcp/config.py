"""
Configuration file for audio_over_tcp program.
This configuration file is for both client and the server, so keep the same file on client and server side.
"""

"""
Configurations for both sides
"""
# Port on which the server is running and client connects to
PORT = 8081

# Audio parameters, do not exceed chunk greater that 4096
CHUNK = 4096
RATE = 44100

"""
Configuration for client side
"""


class Client:
    SERVER_IP = "localhost"
