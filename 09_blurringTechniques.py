import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

"""
How blurring works:
we define kernal size that is window size, and the pixel intensity of the center of the pixel is decided by the surrounding pixels. The window moves sidewards and downwards
"""

# Averaging
"""
In average blur center pixel value is the avg of the surrounding pixels that are in the window size (or kernal size)
"""
average = cv.blur(src=img, ksize=(3, 3))  # more kernal size => more blur
# average = cv.blur(src=img, ksize=(7, 7))  # more kernal size => more blur
cv.imshow("Average Blur", average)

# Gaussian
"""
works same as avg blur but only difference is, instead of caluclating avg of surrounding pixels directly. It gives weights to the surrounding pixels and then calculates avg acc to product. Using this, we get less blurring as compared to avg blur but gaussain blur is more natural
"""
# gauss = cv.GaussianBlur(src=img, ksize=(7, 7), sigmaX=0)
gauss = cv.GaussianBlur(src=img, ksize=(3, 3), sigmaX=0)
cv.imshow("Gaussian Blur", gauss)

# Median blur
"""
same as averaging, but instead of finding avg, it finds the median of the surrounding pixels. Generally median blurring tends to be more effective in reducing the noise as compared to averaging and gaussian blur. Well median bluring are not meant for high kernel sizes like 7 or even 5
"""
# median = cv.medianBlur(src=img, ksize=7)
median = cv.medianBlur(src=img, ksize=3)
cv.imshow("Median blur", median)

# Bilateral Blurring
"""
Traditioanl blurring applies the blurring without seeing whether it is blurring the edges or not. Bilateral blurring applies the blurring but retains the edges
"""
# d = diameter, sigmaSpace basically defines how far the pixel should be considered for blurring or what will be the influence of the far pizels on the center pixel for blurring
# bilateral = cv.bilateralFilter(src=img, d=5, sigmaColor=15, sigmaSpace=15)
bilateral = cv.bilateralFilter(src=img, d=10, sigmaColor=35, sigmaSpace=25)
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)
