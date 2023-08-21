import cv2 as cv

## Reading an image
# img = cv.imread("Photos/imageOne.jpg")

# cv.imshow("Output Image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

## Streaming a video
capture = cv.VideoCapture("Videos/videoTwo.mp4")

while True:
    isTrue, frame = capture.read()

    cv.imshow("Output Video", frame)

    if cv.waitKey(20) == ord("q"):
        break

# capture.release()
# cv.destroyAllWindows()
