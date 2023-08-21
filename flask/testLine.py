import cv2
import numpy as np
from flask import Flask, render_template, Response

app = Flask(__name__)

cap = cv2.VideoCapture(0)
cap.set(3, 560)
cap.set(4, 520)


@app.route("/")
def index():
    return render_template("realtime.html")


def generate_frames():
    while True:
        ret, frame = cap.read()
        low_b = np.uint8([5, 5, 5])
        high_b = np.uint8([0, 0, 0])
        mask = cv2.inRange(frame, high_b, low_b)
        contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                coordinates = "CX : " + str(cx) + "  CY : " + str(cy)

                if cx >= 120:
                    direction = "Turn Left"
                elif cx < 120 and cx > 40:
                    direction = "On Track!"
                else:
                    direction = "Turn Right"

                yield (
                    b"--frame\r\n"
                    b"Content-Type: text/plain\r\n\r\n" + coordinates.encode() + b"\r\n"
                    b"Content-Type: text/plain\r\n\r\n"
                    + direction.encode()
                    + b"\r\n\r\n"
                )

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)
