import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
# img = cv.imread("Photos/lineOne.jpg")
# img = cv.imread("Photos/lineTwo.jpg")
# img = cv.imread("Photos/tokyo.jpg")
cv.imshow("OG Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)


## Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian Image", lap)


## Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", combined_sobel)

cv.waitKey(0)
