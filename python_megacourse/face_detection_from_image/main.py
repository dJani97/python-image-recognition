import cv2 as cv

face_cascade = cv.CascadeClassifier("../haarcascade_frontalface_default.xml")
img = cv.imread("news.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.1,
                                      minNeighbors=5)

for x, y, w, h in faces:
    img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv.imshow("Faces", img)
cv.waitKey(0)
