import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("OG Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Image", blank)

## The height of the image is stored at the index 0.
## The width of the image is stored at index 1.
## The number of channels in the image is stored at index 2.

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)

cv.waitKey(0)
