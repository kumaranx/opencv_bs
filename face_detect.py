import cv2 as cv

# img = cv.imread("Photos/wayne.jpg")
# img = cv.imread("Photos/kOne.jpeg")
# img = cv.imread("Photos/groupTwo.jpg")
img = cv.imread("Photos/groupThree.jpg")
cv.imshow("OG Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

## Haar Cascade
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f"No of faces found = {len(faces_rect)}")

for x, y, w, h in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected Faces", img)
cv.waitKey(0)
