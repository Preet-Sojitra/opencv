import cv2 as cv

"""
    Thresholding is an binarization of an image. In general, we want to take an image and convert it to a binary image
"""

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple thresholding
"""
    cv.threshold takes following arguments:
        - src: source image
        - thresh: threshold value. The pixel value is compared with this value
        - maxval: maximum value. The pixel value is set to this value if it is greater than thresh
        - type: thresholding type
        
    return value:
        - threshold: the threshold value that was used
        - thresh: the thresholded image
        
    Basically, what it does is that, it looks at each pixel of the image and compares its value with the threshold value and if it is greater than the threshold value, it assigns it to the maxval. Otherwise, it assigns it to 0.
"""
threshold, thresh = cv.threshold(
    src=gray, thresh=150, maxval=255, type=cv.THRESH_BINARY
)
cv.imshow("Simple Thresholded", thresh)

# Inverse thresholding
"""
    This is the opposite of simple thresholding. If the pixel value is lower than the threshold value, it assigns it to the maxval. Otherwise, it assigns it to 0.
"""
threshold, thresh_inverse = cv.threshold(
    src=gray, thresh=150, maxval=255, type=cv.THRESH_BINARY_INV
)
cv.imshow("Thresholded Inverse", thresh_inverse)

# Adaptive thresholding
"""
    In adaptive thresholding, we don't hardcode the threshold value. The computer will find the optimal threshold value for us.
    
    - blockSize: the size of the neighborhood area
    - C: a constant that is subtracted from the mean for fine tuning the threshold value
"""
adaptive_thresh = cv.adaptiveThreshold(
    src=gray,
    maxValue=255,
    adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
    thresholdType=cv.THRESH_BINARY,
    blockSize=11,
    C=3,
)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(
    src=gray,
    maxValue=255,
    adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
    thresholdType=cv.THRESH_BINARY_INV,
    blockSize=11,
    C=3,
)
cv.imshow("Adaptive Inverse Thresholding ", adaptive_thresh_inv)

cv.waitKey(0)
