import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

stream = cv2.VideoCapture(0)

while True:
    ret, frame = stream.read()
    frame = cv2.flip(frame, 180)
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('face_detect', frame)
    if cv2.waitKey(1) == 27:
        break

stream.release()
cv2.destroyAllWindows()
