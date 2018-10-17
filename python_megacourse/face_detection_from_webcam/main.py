import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv.VideoCapture(0)

"""
the project will be built here
"""

video.release()