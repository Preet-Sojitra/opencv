import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# splitting the image into individual color channels
b, g, r = cv.split(img)

# cv.imshow("Blue", b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging the color channels
merged = cv.merge([b, g, r])
# cv.imshow("Merged", merged)

# showing the actual color channels with color
# for that we can construct a blank image with the same size as the original image
blank = np.zeros(img.shape[:2], dtype="uint8")

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

cv.waitKey(0)
