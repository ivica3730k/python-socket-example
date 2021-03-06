import cv2
import imagiz

server = imagiz.TCP_Server(8011)
server.start()
while True:
    message = server.receive()
    frame = cv2.imdecode(message.image, 1)
    cv2.imshow(message.client_name, frame)
    cv2.waitKey(1)
