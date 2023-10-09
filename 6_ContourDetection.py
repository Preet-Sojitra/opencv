import cv2 as cv
import numpy as np

# contours are bascially the boundaries of objects. They are not same as edges. From mathematical pov they are not same

img = cv.imread("Photos/cats.jpg")
cv.imshow("Pussy", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny edges", canny)

# takes canny as input
# returns list of contours and hirearchies (hierarchies are out of scope as of now)
# cv.Reterlist is a mode in which findContours method returns and find the contours. ReterList returns all the contours that are find in the image.
# Other values for mode:
# cv.reter_external returns only external contours
# cv.reter_tree returns all the hierarchical contours
# cv.chain_approx_none is the contour approximation method. It is bascailly how we want to approximate the contour
# chain_approx_none does nothing
# many people prefer to use cv.CHAIN_APPROX_SIMPLE which essentially compress contoures into a simple one that makes more sense
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# since contours is a list, we can find the length to find how many contours detected
# print(f"{len(contours)} contour(s) found")

# with blur it found 380, without blurred it found apprx 2700 contours


# There is another method of finding contours instead of using blur and edges, that is by using threshold

ret, thresh = cv.threshold(
    gray, 125, 255, type=cv.THRESH_BINARY
)  # threshold binarize the image. If pxiel value is below 125 , it is set to 0, if above it is set to 255 (that is 1)
cv.imshow("Thres", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# since contours is a list, we can find the length to find how many contours detected
print(f"{len(contours)} contour(s) found")

# drawing contours to blank image that are found
# takes image to draw contour on, takes list of contours, takes the index of contours that is how many contours to draw (-1 for drawing all contours), color of the contour and the thickness
cv.drawContours(
    image=blank, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=1
)
cv.imshow("Contours drawn", blank)

cv.waitKey(0)
