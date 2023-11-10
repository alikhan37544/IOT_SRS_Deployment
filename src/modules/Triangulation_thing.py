import cv2
import numpy as np
import tkinter as tk

# Function to detect faces and hands in the frame
def detect_faces_hands(frame, face_cascade, hand_cascade, num_zones):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

    zones = np.array_split(np.arange(frame.shape[1]), num_zones)  # Divide frame into zones
    detected_zones = set()

    # Check for detected faces and hands in each zone
    for face in faces:
        (x, y, w, h) = face
        face_center_x = x + w // 2
        for i, zone in enumerate(zones):
            if face_center_x in zone:
                detected_zones.add(i)
                break

    for hand in hands:
        (x, y, w, h) = hand
        hand_center_x = x + w // 2
        for i, zone in enumerate(zones):
            if hand_center_x in zone:
                detected_zones.add(i)
                break

    return detected_zones

# Function to update the video feed with highlighted zones
def update_video_feed():
    ret, frame = cap.read()

    detected_zones = detect_faces_hands(frame, face_cascade, hand_cascade, num_zones)

    for i, zone in enumerate(zones):
        color = (0, 0, 255) if i in detected_zones else (0, 255, 0)
        cv2.rectangle(frame, (zone[0], 0), (zone[1], frame.shape[0]), color, 2)

    # Display the updated frame
    cv2.imshow("Zoned Detection", frame)

    # Call the function again after 10 milliseconds
    root.after(10, update_video_feed)

# Function to update the number of zones based on user input
def update_zones():
    global num_zones, zones
    num_zones = int(entry.get())
    zones = np.array_split(np.arange(screen_width), num_zones)
    cap.set(3, screen_width)  # Set camera width
    cap.set(4, screen_height)  # Set camera height
    entry.delete(0, tk.END)  # Clear the entry field

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

# Load Haar cascades for face and hand detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_hand.xml')

# Initialize Tkinter GUI
root = tk.Tk()
root.title("Zone Detection")

# Ask for the number of zones using GUI
label = tk.Label(root, text="Enter number of zones:")
label.pack(side=tk.LEFT)
entry = tk.Entry(root)
entry.pack(side=tk.LEFT)
update_button = tk.Button(root, text="Update Zones", command=update_zones)
update_button.pack(side=tk.LEFT)

# Set screen dimensions and zones based on user input
screen_width = 640
screen_height = 480
num_zones = 1
zones = np.array_split(np.arange(screen_width), num_zones)

# Start updating the video feed
update_video_feed()

# Run Tkinter main loop
root.mainloop()

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
