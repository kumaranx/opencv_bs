import cv2 as cv


# img = cv.imread("Photos/cats.jpg")
# img = cv.imread("Photos/tokyo.jpg")
img = cv.imread("Photos/lineOne.jpg")
# img = cv.imread("Photos/lineTwo.jpg")
# img = cv.imread("Photos/lineThree.jpg")
cv.imshow("OG Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

## The main purpose of thresholding is to separate regions of interest from the background or to convert grayscale images into binary images.

## Object Detection and Tracking: In computer vision tasks like object detection and tracking, thresholding can be used to create binary masks of objects, which makes it easier to identify and track them.

## Edge Detection: Thresholding can be used as a preliminary step for edge detection algorithms. By converting an image to binary, it becomes easier to find edges or contours of objects in the scene.


## Simple Thresholding
threshold, thresh = cv.threshold(
    gray, 150, 255, cv.THRESH_BINARY
)  ## 150 -> value of avg intensity threshold, if single pixel > 150, pixel is set to 255(white), < 150 pixel is set to 0(black)
cv.imshow("Simple Thresholded", thresh)

print(threshold)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholding Inverse", thresh_inv)


## Adaptive Thresholding
adaptive_threshold = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9
)  ## 11 is the kernel size/ block size, 9 is a constant value subtracted from the mean
cv.imshow("Adaptive Thresholding", adaptive_threshold)

adaptive_threshold_inv = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 13, 9
)
cv.imshow("Adaptive Thresholding Inverse", adaptive_threshold_inv)

cv.waitKey(0)
