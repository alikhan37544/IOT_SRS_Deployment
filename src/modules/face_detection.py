import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from keras.models import load_model
from keras.applications.inception_resnet_v2 import preprocess_input

# Load FaceNet model
face_net_model = load_model("facenet_weights.h5")

# Load face cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to recognize face using FaceNet model
def recognize_face(img):
    img = cv2.resize(img, (160, 160))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    embedding = face_net_model.predict(img)
    # Compare embedding with known embeddings and return the recognized person's name
    # Replace this logic with your dataset and recognition mechanism
    recognized_person_name = "John Doe"  # Replace with actual recognized person's name
    return recognized_person_name

# Function to detect and recognize faces in the video feed
def detect_and_recognize_faces():
    # Open a connection to the default camera (camera index 0)
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame using the face cascade
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Loop through detected faces and recognize them
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            recognized_person_name = recognize_face(face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f"Verified: {recognized_person_name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Display the frame with recognized faces
        cv2.imshow("Face Recognition", frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Function to open a GUI window and call detect_and_recognize_faces function
def open_gui():
    root = tk.Tk()
    root.title("Face Recognition")

    # Button to detect and recognize faces
    detect_button = tk.Button(root, text="Detect and Recognize Faces", command=detect_and_recognize_faces)
    detect_button.pack(side="bottom", fill="both", expand="yes")

    # Run Tkinter main loop
    root.mainloop()

# Call the function to open the GUI
open_gui()
