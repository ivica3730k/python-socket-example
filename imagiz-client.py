import cv2

cap = cv2.VideoCapture("/dev/video2")
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('U', 'Y', 'V', 'Y'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2304)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1536)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

i = 0
while True:
    try:
        r, frame = cap.read()
    except cv2.error:
        continue
    cv2.imshow("s", frame)
    cv2.imwrite(str(i) + ".jpg", frame)
    cv2.waitKey(1)
    i += 1
    if i > 10:
        break
