import cv2 as cv
import numpy as np

# img = cv.imread("Photos/cats.jpg")
# img = cv.imread("Photos/imageFive.jpg")
img = cv.imread("Photos/lineOne.jpg")
# img = cv.imread("Photos/imageSix.jpg")
cv.imshow("OG Image", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

## Contours are the outline or curve, joins the points along the boundary, diff from edges

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur Image", blur)

canny = cv.Canny(blur, 125, 175)  ## use canny instead of thresholding
cv.imshow("Canny Image", canny)

## using threshold instead of canny
ret, thresh = cv.threshold(
    gray, 125, 225, cv.THRESH_BINARY
)  ## density of pixel < 125 set to 0(black), > 125 set to 255(white)
cv.imshow("Threshold Image", thresh)

contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour's were found !")

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours", blank)

cv.waitKey(0)
