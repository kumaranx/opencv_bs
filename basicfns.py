import cv2 as cv
import numpy as np

img = cv.imread("Photos/tokyo.jpg")
cv.imshow("og image", img)

## Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

## Blur (used to reduce the noise in the img)
## using Gaussian Blur
blur = cv.GaussianBlur(
    img, (3, 3), cv.BORDER_DEFAULT
)  ## kernel size (3,3) intensity of the blur
cv.imshow("Blur", blur)

## Edge Cascade
## using Canny Edge Detector
canny = cv.Canny(img, 125, 175)  ## higher edges can be removed using blur
cv.imshow("Canny", canny)

## Dilating the image
dilated = cv.dilate(
    canny, (7, 7), iterations=3
)  ## iterations specify the no of time a fn to be run
cv.imshow("Dilated", dilated)

## Eroding (used to convert the dilated img to previous state)
eroded = cv.erode(dilated, (5, 5), iterations=2)
cv.imshow("Eroded", eroded)

# ## Resizing the image
# resized = cv.resize(img, (500, 350), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)

# ## Cropping the image
# cropped = img[225:335, 370:470]
# cv.imshow("Cropped", cropped)
cv.waitKey(0)
