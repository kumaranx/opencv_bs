import os
import cv2 as cv
import numpy as np

# people = ["Cillian Murphy", "Robert Pattinson"]

people = []
for i in os.listdir(
    r"/home/cullen/Documents/projectS7/opencv/fccBs/Train"
):  ## r-> raw string
    people.append(i)

DIR = r"/home/cullen/Documents/projectS7/opencv/fccBs/Train/"

haar_cascade = cv.CascadeClassifier("haar_face.xml")

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4
            )

            for x, y, w, h in faces_rect:
                face_roi = gray[
                    y : y + h, x : x + w
                ]  ## roi -> region of interest, crop out the faces of the img y to y + height & x to x + width
                features.append(faces_rect)
                labels.append(
                    label
                )  ## the label represents the index of the person associated with the detected face. This index will be used as the label for the corresponding face data in the features list.


create_train()
print("Training Done -----------------------")

features = np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

## Train the recognizer on the features and labels list
face_recognizer.train(features, labels)

# np.save("features.npy", features)
# np.save("labels.npy", labels)
