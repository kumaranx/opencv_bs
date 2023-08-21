import cv2 as cv
import numpy as np

img = cv.imread("Photos/tokyo.jpg")

cv.imshow("OG Image", img)


## Translation  (shifting the img in x & y directions)
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])  ## 1 is the width & 0 is the height
    return cv.warpAffine(img, transMat, dimensions)

## The height of the image is stored at the index 0.
## The width of the image is stored at index 1.
## The number of channels in the image is stored at index 2.

## -x -> left
## -y -> up
##  x -> right
##  y -> down

translated = translate(img, -100, -100)
cv.imshow("Translated", translated)


## Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[
        :2
    ]  ## :2 takes the first two values of the shape height & width
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 90)
cv.imshow("Rotated", rotated)


## Resizing
resized = cv.resize(img, (500, 400), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)


## Flipping
flip = cv.flip(
    img, 1
)  ## 0 to flip horizontally, 1 to flip vertically, -1 to flip in both directions
cv.imshow("Flipped", flip)


## Cropping
cropped = img[220:330, 375:485]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
