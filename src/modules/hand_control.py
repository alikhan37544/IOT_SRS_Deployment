import cv2
import numpy as np
import tkinter as tk

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

# Load Haar cascade for hand detection
hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '/home/akz/Programming/Raspi/IOT_SRS_Deployment/src/modules/haarcascades_hand.xml')

# Function to detect open or closed hand
def detect_hand_status(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

    if len(hands) > 0:
        (x, y, w, h) = hands[0]
        hand_roi = gray[y:y + h, x:x + w]
        _, hand_threshold = cv2.threshold(hand_roi, 127, 255, cv2.THRESH_BINARY_INV)

        # Calculate the percentage of white pixels in the hand region
        hand_area = cv2.countNonZero(hand_threshold)
        hand_percentage = (hand_area / (w * h)) * 100

        # If more than 70% of hand is open, return "Open", otherwise return "Closed"
        return "Open" if hand_percentage > 70 else "Closed"
    else:
        return "No Hand"

# Function to update the virtual bulb status based on hand status
def update_bulb_status():
    _, frame = cap.read()
    hand_status = detect_hand_status(frame)
    
    bulb_status_label.config(text=f"Hand Status: {hand_status}")

    # If hand is open, turn on the virtual bulb, otherwise turn it off
    if hand_status == "Open":
        bulb_canvas.itemconfig(bulb_image, image=bulb_on_image)
    else:
        bulb_canvas.itemconfig(bulb_image, image=bulb_off_image)

    # Call the function again after 10 milliseconds
    root.after(10, update_bulb_status)

# Initialize Tkinter GUI
root = tk.Tk()
root.title("Virtual Bulb")

# Load images for bulb on and off states
bulb_on_image = tk.PhotoImage(file="/home/akz/programming/IOT_SRS_Deployment/src/modules/bulb_on.png")
bulb_off_image = tk.PhotoImage(file="/home/akz/programming/IOT_SRS_Deployment/src/modules/bulb_off.png")

# Create a canvas to display the bulb
bulb_canvas = tk.Canvas(root, width=bulb_on_image.width(), height=bulb_on_image.height())
bulb_canvas.pack()

# Display the bulb off image initially
bulb_image = bulb_canvas.create_image(0, 0, anchor=tk.NW, image=bulb_off_image)

# Label to display hand status
bulb_status_label = tk.Label(root, text="Hand Status: No Hand", font=("Helvetica", 16))
bulb_status_label.pack()

# Start updating the bulb status
update_bulb_status()

# Run Tkinter main loop
root.mainloop()

# Release the camera
cap.release()
