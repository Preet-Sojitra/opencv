import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
# cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
lap = cv.Laplacian(src=gray, ddepth=cv.CV_64F)  # type: ignore
lap = np.uint8(np.absolute(lap))
# cv.imshow("Laplacian", lap)  # type: ignore

# Sobel
"""
    Sobel computes the gradient in two directions: X and Y
"""
sobelx = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0)  # type: ignore
sobely = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1)  # type: ignore
cv.imshow("Sobel_X", sobelx)
cv.imshow("Sobel_Y", sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("Combined Sobel", combined_sobel)

cv.waitKey(0)
