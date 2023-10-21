import cv2 as cv

# img = cv.imread("Photos/lady.jpg")
# img = cv.imread("Photos/group 2.jpg")
img = cv.imread("Photos/group 1.jpg")  # more complex
# cv.imshow("Person", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray person", gray)
cv.imshow("Gray people", gray)

# Used the pretrained haarcascade classifier from opencv
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f"Number of faces found = {len(faces_rect)}")
print(faces_rect)

for x, y, w, h in faces_rect:
    cv.rectangle(
        img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2
    )

cv.imshow("Deteced Faces", img)

cv.waitKey(0)
