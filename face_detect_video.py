import cv2 as cv

# Load the Haar Cascade classifier
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Open the video file
video_path = "Videos/videoFour.mp4"
# video_path = "Videos/videoFive.mp4"
# cap = cv.VideoCapture(video_path)
cap = cv.VideoCapture(2)

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=11)

    # Draw rectangles around the detected faces
    for x, y, w, h in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    # Display the frame with detected faces
    cv.imshow("Detected Faces", frame)

    # Check for the 'q' key to exit the video loop
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv.destroyAllWindows()
