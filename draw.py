import cv2 as cv
import numpy as np

blank = np.zeros(
    (500, 500, 3), dtype="uint8"
)  ## height, width & no of color channels (BGR -> 3)
cv.imshow("blank", blank)

## Paint the image of certain color
blank[200:300, 300:400] = 0, 255, 0  ## range of pixels(y, x) & bgr value
cv.imshow("green", blank)

## Rectangle
cv.rectangle(
    blank,
    (0, 0),
    (250, 250),
    (0, 0, 255),
    thickness=cv.FILLED,  ## point 1 coordinates(0,0) & point 2 coordinates(250,250)
)  ## thickness=z 'z' specifies the border thickness
cv.imshow("rectangle", blank)

## The height of the image is stored at the index 0.
## The width of the image is stored at index 1.
## The number of channels in the image is stored at index 2.

## Circle
cv.circle(
    blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 255, 0), thickness=-1
)
cv.imshow("circle", blank)

## Line
cv.line(blank, (0, 250), (250, 0), (255, 0, 0), thickness=2)
cv.imshow("line", blank)

## Text

# cv.putText(
#     blank, "Hola", (225, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2
# )  ## font size -> 1.0 to scale the font
# cv.imshow("line", blank)

cv.waitKey(0)
