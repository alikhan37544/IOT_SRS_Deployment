import cv2
import numpy as np

# Initialize camera
cap = cv2.VideoCapture(0)

# Variable to store the static background frame
static_frame = None

while True:
    # Read frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Set static frame (background) for motion detection
    if static_frame is None:
        static_frame = gray_frame
        continue

    # Compute absolute difference between current frame and static frame
    frame_delta = cv2.absdiff(static_frame, gray_frame)
    thresh_frame = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Find contours of the detected motion
    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the detected motion
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Display the frames
    cv2.imshow("Motion Detection", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
