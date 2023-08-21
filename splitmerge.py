import cv2 as cv
import numpy as np

img = cv.imread("Photos/tokyo.jpg")
cv.imshow("OG Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, b, blank])
red = cv.merge([blank, blank, b])

cv.imshow("Blue Graded", blue)
cv.imshow("Green Graded", green)
cv.imshow("Red Graded", red)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

cv.waitKey(0)
