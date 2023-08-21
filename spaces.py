import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/tokyo.jpg")
cv.imshow("OG Image", img)

# plt.imshow(img)
# plt.show()

## BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

## BGR to HSV    (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Image", hsv)

## BGR to LAB  (l*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB Image", lab)

##  opencv uses bgr image format, matplotlib uses rgb

## BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB Image", rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)
