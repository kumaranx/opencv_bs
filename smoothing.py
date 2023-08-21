import cv2 as cv


img = cv.imread("Photos/cats.jpg")
cv.imshow("OG Image", img)

## Averaging   --->    (it uses the avg kernel size intensity value to middle pixel to blur)
average = cv.blur(img, (7, 7))
cv.imshow("Average Blur", average)

## Gaussian Blur  ---> (it uses weight value of each kernel combined, it is more natural than average blur)
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian Blur", gaussian)

## Median Blur ---> (effetive than averaging in reducing noise)
median = cv.medianBlur(img, 7)
cv.imshow("Median Blur", median)

## Bilateral Blur --->  (effective than others)
bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)
