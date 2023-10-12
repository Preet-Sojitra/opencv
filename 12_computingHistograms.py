import cv2 as cv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
    Computing histograms allows us to visualize the distribution of pixel intensities in an image. Whether it is color image or grayscale image, we can use the same function to compute the histogram of the image. It gives high level idea about the intensity distribution of the image. It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis and corresponding number of pixels in the image on Y-axis.
"""

img = cv.imread("Photos/cats_2.jpg")
# cv.imshow("Cats", img)

# Starting with computing histogram of a grayscale image
# gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Grayscale histogram
"""
    calcHist takes following parameters:
    - list of images
    - list of channels: The index of channel for which we calculate histogram. For grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
    - mask: If a mask is provided, a histogram will be computed for masked pixels only. If we do not want to use mask, we can pass "None".
    - histSize: It is the number of bins we want to use when computing a histogram. For full scale, we pass [256].
    - ranges: This is our range. Normally, it is [0, 256].
"""
# gray_hist = cv.calcHist(
#     images=[gray], channels=[0], mask=None, histSize=[256], ranges=[0, 256]
# )

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Histogram on masked image
blank = np.zeros(img.shape[:2], dtype="uint8")

mask = cv.circle(img=blank, center=(img.shape[1] // 2, img.shape[0] // 2), radius=100, color=255, thickness=-1)  # type: ignore
# cv.imshow("Mask", mask)

# gray_mask_hist = cv.calcHist(
#     images=[gray], channels=[0], mask=mask, histSize=[256], ranges=[0, 256]
# )

# plt.figure()
# plt.title("Grayscale Mask Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_mask_hist)
# plt.xlim([0, 256])
# plt.show()

# Color histogram
colors = ("b", "g", "r")  # tuple of colors

plt.figure()
plt.title("Grayscale Mask Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
for i, col in enumerate(colors):
    hist = cv.calcHist(
        images=[img], channels=[i], mask=None, histSize=[256], ranges=[0, 256]
    )
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
