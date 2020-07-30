import cv2
import imagiz

server = imagiz.Server()
while True:
    message = server.receive()
    cv2.imshow(message.client_name, message.image)
    cv2.waitKey(1)
