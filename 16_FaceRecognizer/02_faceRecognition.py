import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier("../haar_face.xml")

DIR = "../Faces/train"

people = []
for i in os.listdir(DIR):
    people.append(i)

# features = np.load("features.npy")
# labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()  # type: ignore

face_recognizer.read("face_trained.yml")

img = cv.imread("../Faces/val/elton_john/1.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

# Detect the face in image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for x, y, w, h in faces_rect:
    faces_roi = gray[y : y + h, x : x + h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Lable = {people[label]} with confidence of {confidence}")

    cv.putText(
        img,
        str(people[label]),
        (20, 20),
        cv.FONT_HERSHEY_COMPLEX,
        fontScale=1.0,
        color=(0, 255, 0),
    )
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected Face", img)


cv.waitKey(0)
