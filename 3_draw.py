import cv2 as cv
import numpy as np

# To draw we can make blank image or draw on existing image

# blank image
blank = np.zeros((500, 500, 3), dtype="uint8")  # uint8 is the dtype for image
# cv.imshow("Blank", blank)

# 1. Paint the image a certain color
# blank[:] = 0, 255, 0  # painting entire image green
# cv.imshow("Green", blank)

# 2. Painting certain portion
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow("Red", blank)

# 3. Draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow("Rectangle", blank)

# 4. We can fill in the rectangle using
# cv.rectangle(
#     blank, (0, 0), (250, 500), (0, 255, 0), thickness=cv.FILLED
# )  # or instead of cv.FILLED we can also specify thickness as -1 to fill
# cv.imshow("Rectangle", blank)

# 5. Draw a circle
# cv.circle(blank, center=(250, 250), radius=40, color=(0, 0, 255), thickness=3)
# cv.circle(blank, center=(250, 250), radius=40, color=(0, 0, 255), thickness=-1)
# cv.imshow("circle", blank)

# 6. Draw a line
# cv.line(blank, (0, 0), (250, 250), color=(255, 255, 255), thickness=3)
# cv.imshow("Line", blank)

# 7. Write text
cv.putText(
    blank,
    "Hello World",
    (225, 225),
    fontFace=cv.FONT_HERSHEY_TRIPLEX,
    fontScale=1.0,
    color=(0, 255, 0),
    thickness=2,
)
cv.imshow("Text", blank)

# or we can draw on this cat image also
# img = cv.imread("Photos/cat.jpg")
# cv.imshow("Cat", img)

cv.waitKey(0)
