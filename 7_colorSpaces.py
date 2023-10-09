import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# Run below two line in ipynb or interactive python shell to see the image because it is having an error in showing image in python script
# plt.imshow(img)
# plt.show()

# above output explained:
"""
    The image of matplotlib is in RGB format and the image of OpenCV is in BGR format. Thus the image of matplotlib will be compeletely inverse of the image of OpenCV. 
    Opencv reads in BGR format and matplotlib reads in RGB format. That's why matplotlib doesn't know that the image is in BGR format and it will show the image in RGB format. Thus inversion.
"""

# BGR (default way of reading image in OpenCV) to Grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, code=cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB (or L*a*b)
lab = cv.cvtColor(img, code=cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rbg = cv.cvtColor(img, code=cv.COLOR_BGR2RGB)
cv.imshow("RGB", rbg)  # this rbg will be same as the image of matplotlib

# One downside: we cannot convert grayscale to hsv directly. We have to convert it to BGR first and then to HSV

cv.waitKey(0)
