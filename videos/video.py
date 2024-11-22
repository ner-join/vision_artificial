import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    cv2.imshow('First Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
capture.release()