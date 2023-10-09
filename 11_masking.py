import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

"""
    Using Bitwise operators we can essentially perform masking. Masking allows us to focus on certain parts of image that we want to focus on. 
"""

blank = np.zeros(
    img.shape[:2], dtype="uint8"
)  # IMP: dimensions of the mask has to be same as that of the image

# mask = cv.circle(img=blank, center=(img.shape[1] // 2, img.shape[0] // 2), radius=100, color=255, thickness=-1)  # type: ignore
# mask = cv.circle(img=blank, center=(img.shape[1] // 2 + 45, img.shape[0] // 2), radius=100, color=255, thickness=-1)  # type: ignore
# cv.imshow("Mask", mask)

# masked = cv.bitwise_and(src1=img, src2=img, mask=mask)
# cv.imshow("Masked image", masked)

# bitwise multiple shapes to create weird shape and use it as mask

circle = cv.circle(img=blank.copy(), center=(img.shape[1] // 2 + 45, img.shape[0] // 2), radius=100, color=255, thickness=-1)  # type: ignore

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird Shape", weird_shape)

masked = cv.bitwise_and(src1=img, src2=img, mask=weird_shape)
cv.imshow("Masked image", masked)

cv.waitKey(0)
