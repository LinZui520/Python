import cv2

face_cascade = cv2.CascadeClassifier('RecognitionModel.xml')

stream = cv2.VideoCapture(0)

while True:
    ret, frame = stream.read()
    frame = cv2.flip(frame, 180)
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        width = x + w
        height = y + h
        color = (255, 0, 0)
        cv2.rectangle(frame, (x, y), (width, height), color, 2)

    cv2.imshow('face_detect', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
