import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)


# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # type: ignore
    # print(transMat)
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)  # type:ignore


# -x => left, -y => up, x => right, y => down
translated = translate(img, -100, 100)
cv.imshow("Translated", translated)


# Rotation
def rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]

    if rotationPoint is None:
        rotationPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotationPoint, angle=angle, scale=1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# positive angle rotated counterclockwise and negative rotaties clockwise
rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow("Rotated Rotated Image", rotated_rotated)

# Flipping
# flipCode = 0 || 1 || -1
# 0 => flips over Y axis , 1 => X axis , -1 => both X and y
flip = cv.flip(img, flipCode=-1)
cv.imshow("Flipped", flip)

cv.waitKey(0)
