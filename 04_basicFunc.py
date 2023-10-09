import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("boston", img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("boston Grey image", gray)

# Blur an image
# TODO: Read more about gussian blur later
# blur = cv.GaussianBlur(
#     img, (3, 3), cv.BORDER_DEFAULT
# )  # ksize = kernal size. It is tuple with odd nos. More details later
# to increase the blur we can increase the kernal size
# cv.imshow("Blurred", blur)

# more_blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("More blur", more_blur)

# Edge Cascade
# Fining the edges that are present in the image
# cany = cv.Canny(img, 125, 175)
# cv.imshow("Canny", cany)

# we can reduce some of the images by blurring the image. Instead of passing img, we will pass blur img
# less_edges_cany = cv.Canny(more_blur, 125, 175)
# cv.imshow("Less Edges Canny", less_edges_cany)

# Dialating the image
# takes canny image as input
# dilated = cv.dilate(less_edges_cany, (7, 7), iterations=3)  # type: ignore
# cv.imshow("Dilated", dilated)

# Eroding (it is bascially for getting edges back)
# takes dilated image as input
# eroded = cv.erode(dilated, (3, 3), iterations=1)  # type: ignore
# cv.imshow("Erdoded", eroded)

# Resize
# there is also one interpolation parameter that is super useful.
# if we are resizing to lesser dimension than original then INTER_AREA is useful
# if enarlaring to scaling to much larger, then INTER_LINEAR or INTER_CUBIC is userful. Cubic is slow but quality is supberb
# resized = cv.resize(img, (500, 500))  # resize to 500x500 ignoring the aspcet ratio
# cv.imshow("resize", resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
