"""
Configuration file for serial_over_tcp program.
This configuration file is for both client and the server, so keep the same file on client and server side.
"""

"""
Configurations for both sides
"""
# Port on which the server is running and client connects to
PORT = 8080
# Set to TRUE if you know that your serial devices output proper line termination to enhance transfer speeds
OPTIMIZE_FOR_SERIAL_LINES = False
"""
Configuration for server side
"""


class Server:
    # Serial port which you want to use on the server side
    SERIAL_PORT = "/dev/ttyUSB0"
    # Baud for the chosen serial port
    SERIAL_BAUD = 9600


"""
Configuration for client side
"""


class Client:
    SERVER_IP = "localhost"
    # Serial port which you want to use on the client side
    SERIAL_PORT = "/dev/ttyUSB1"
    # Baud for the chosen serial port
    SERIAL_BAUD = 9600
