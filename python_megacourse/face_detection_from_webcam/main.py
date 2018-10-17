import cv2 as cv

face_cascade = cv.CascadeClassifier("../haarcascade_frontalface_default.xml")
video = cv.VideoCapture(0)
capturing = True

while capturing:
    check, frame = video.read()
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img,
                                          scaleFactor=1.2,
                                          minNeighbors=5)

    for x, y, w, h in faces:
        img = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv.imshow("Webcam 1", frame)
    key = cv.waitKey(10)
    if key == ord('q'):
        capturing = False

video.release()
cv.destroyAllWindows()