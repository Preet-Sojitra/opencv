import cv2 as cv


# Below function works for Images, Videos and Live Videos. Basically for everything
def rescale(frame, scale=0.75):
    # print(frame.shape)  # first is height, and 2nd is width
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


"Rescaling image"
# img = cv.imread("Photos/cat.jpg")

# new_img = rescale(img)
# cv.imshow("Cat", img)
# cv.imshow("Cat_Resized", new_img)

# cv.waitKey(0)

"Rescaling Videos"

capture = cv.VideoCapture("Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()

    frame_resized = rescale(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video_Resized", frame_resized)

    if cv.waitKey(2) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()


"Changing Resolution"


# Below works only for Live Video
def changeRes(width, height):
    capture.set(3, width)  # 3 references the width
    capture.set(4, height)  # 4 references the height
    # we can even change brightness, by 10 (maybe)
