import cv2 as cv

"Reading Images"
# img = cv.imread("Photos/cat.jpg")  # read the image
# img = cv.imread("Photos/cat_large.jpg")  # read the image
# the above image is too large for the screen to accomodate, hence it won't show the image properly
# cv.imshow("Cat", img)  # opens the image in window
# cv.waitKey(0)

"Reading Videos"
# VideoCapture takes path of video or int values like 0,1,2,3. Int values will be used when we want to use the webcam or the cams that our system has
capture = cv.VideoCapture("Videos/dog.mp4")

"""
Explaination of below code:

First we created an instance of VideoCapture and stored in in variable `capture`.
Then we can read the video frame by frame.
`capture.read()` reads the frame and returns two values, one is whether frame has been read successfully and 2nd whether the frame

Then we can dispaly each frame using `imshow()`

To stop the video from playing infinitely we added one condation that, if waitKey is 20 milliseconds and the key pressed is "d" then, break.

Finally we released the capture device and destoryed all windows
"""

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(2) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()

"""
Output of above code:

This will play the video, but once video completed, it will automatically close the window and throw error (-215: Assertion Failed). This means it wasn't able to find any media frame and thus is broke the while loop on its own.
"""
