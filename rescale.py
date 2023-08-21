import cv2 as cv


## function to rescale images, videos, live video
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


cv.waitKey(0)


## function to rescale live video
# def changeRes(width, height):
#     capture.set(3, width)
#     capture.set(4, height)


## Reading image
# img = cv.imread("Photos/imageTwo.jpg")
# resized_img = rescaleFrame(img)

# cv.imshow("image", img)
# cv.imshow("Resized image", resized_img)

# cv.waitKey(0)
# cv.destroyAllWindows()

## Reading video
# capture = cv.VideoCapture("Videos/videoOne.mp4")

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow("Video", frame)
#     cv.imshow("Rescaled Video", frame_resized)

#     if cv.waitKey(20) == ord("q"):
#         break

# capture.release()
# cv.destroyAllWindows()
