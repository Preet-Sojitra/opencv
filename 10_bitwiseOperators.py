import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(
    img=blank.copy(), center=(200, 200), radius=200, color=255, thickness=-1  # type: ignore
)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise: AND
bitwise_and = cv.bitwise_and(src1=rectangle, src2=circle)
cv.imshow("Bitwise AND", bitwise_and)  # returns intersecting portion

# bitwise: OR
bitwise_or = cv.bitwise_or(src1=rectangle, src2=circle)
cv.imshow("Bitwise OR", bitwise_or)  # return all portion

# bitwise: XOR
bitwise_xor = cv.bitwise_xor(src1=rectangle, src2=circle)
cv.imshow("Bitwise XOR", bitwise_xor)  # return non intersecting regions

# bitwise: Not
bitwise_not = cv.bitwise_not(src=rectangle)
cv.imshow("Bitwise Rectangle NOT", bitwise_not)  # return inverse

cv.waitKey(0)
