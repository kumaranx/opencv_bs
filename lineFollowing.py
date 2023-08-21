import cv2
import numpy as np

cap = cv2.VideoCapture(0)

## to change the output window size
cap.set(3, 560)
cap.set(4, 520)


with open("data.csv", "w") as file:
    pass

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

            # with open("data.csv", "w") as file:
            #     pass

            coordinates = "CX : " + str(cx) + "  CY : " + str(cy) + "\n"

            f = open("data.csv", "a")
            f.write(coordinates)

            if cx >= 120:
                print("Turn Left")
                f.write("Turn Left")

            if cx < 120 and cx > 40:
                print("On Track!")
                f.write("On Track!")

            if cx <= 40:
                print("Turn Right")
                f.write("Turn Right")

            f.close()
            cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)

        cv2.drawContours(frame, c, -1, (0, 255, 0), 1)
        cv2.imshow("Mask", mask)
        cv2.imshow("Frame", frame)
    else:
        print("I don't see the line")

    if cv2.waitKey(1) & 0xFF == ord("q"):  # 1 is the time in ms
        break
cap.release()
cv2.destroyAllWindows()
