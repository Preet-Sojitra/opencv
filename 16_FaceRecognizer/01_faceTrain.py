import os
import cv2 as cv
import numpy as np

DIR = "../Faces/train"

people = []
for i in os.listdir(DIR):
    people.append(i)

# print(people)

haar_cascade = cv.CascadeClassifier("../haar_face.xml")
features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        # now we will loop over every image inside that folder
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4
            )

            for x, y, w, h in faces_rect:
                # roi = region of interest
                faces_roi = gray[y : y + h, x : x + h]  # type: ignore
                features.append(faces_roi)  # type: ignore
                labels.append(label)  # type: ignore


create_train()
print("Dataset created ----------------")

# print(f"Length of the features = {len(features)}")
# print(f"Length of the labels = {len(labels)}")

features = np.array(features, dtype="object")
labels = np.array(labels)

# Now we have created our dataset. So we can train our recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()  # type: ignore

# Train the recognizer
face_recognizer.train(features, labels)

face_recognizer.save("face_trained.yml")

np.save("features.npy", features)
np.save("labels.npy", labels)
