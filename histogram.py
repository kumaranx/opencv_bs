import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/cats.jpg")
# img = cv.imread("Photos/tokyo.jpg")
cv.imshow("OG Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale Image", gray)

circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow("Mask", mask)

## histogram allows to visualize the distribution of pixel intensities in a img, in a form of graph/plot
## Histograms can help determine the appropriate threshold value by analyzing the pixel intensity distribution

## Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])  ## 256 = no of bins

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("No of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

## Color Histogram

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow("Mask", mask)

colors = ("b", "g", "r")

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])


##  ref = (# 1. `colors`: It seems that `colors` is a list or iterable containing the colors you want to use for plotting the histograms. For example, it could be a list of strings representing colors like `['blue', 'green', 'red']`.

# 2. `enumerate(colors)`: This line uses the `enumerate` function to iterate through the `colors` list, providing both the index `i` and the color value `col` for each iteration.

# 3. `hist = cv.calcHist([img], [i], None, [256], [0, 256])`: This line calculates the histogram for the `img` (image) for the specific color channel identified by the index `i`. It uses the `cv.calcHist` function from OpenCV, which computes the histogram for one or more images.

#    - `img`: The image for which the histogram is calculated.
#    - `[i]`: The channel index for which the histogram is calculated. For example, 0 for Blue, 1 for Green, and 2 for Red channels in a standard BGR image.
#    - `None`: The mask to be applied. In this case, it's set to `None`, meaning the histogram is calculated for the entire image without any masking.
#    - `[256]`: The number of bins for the histogram. In this case, it's set to 256, which means the histogram will have 256 bins.
#    - `[0, 256]`: The range of pixel values for the histogram. In this case, it's set to [0, 256], indicating the full range of pixel values from 0 to 255.

# 4. `plt.plot(hist, color=col)`: This line uses Matplotlib to plot the histogram data `hist` with the specified color `col`. The `hist` variable contains the histogram values computed in the previous step for a specific color channel.

# 5. `plt.xlim([0, 256])`: This line sets the x-axis limits of the plot to [0, 256]. This ensures that the histogram covers the full range of pixel values from 0 to 255 on the x-axis.

# By running this code, you will get a plot showing the histograms for each color channel (assuming the `colors` list contains appropriate color names) in the image specified by the `img` variable. The x-axis will represent the pixel values from 0 to 255, and the y-axis will represent the frequency of occurrence for each pixel value in the image for each color channel.
# )

plt.show()
cv.waitKey(0)
