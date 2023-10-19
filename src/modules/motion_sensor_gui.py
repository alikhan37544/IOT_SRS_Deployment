# motion_sensor_gui.py

import tkinter as tk
from motion_sensor import MotionSensor

class MotionSensorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Motion Sensor")

        self.motion_sensor = MotionSensor(gui_mode=True)

        self.motion_label = tk.Label(master, text="Motion Sensor Status:")
        self.motion_label.pack()

        self.motion_state_label = tk.Label(master, text="")
        self.motion_state_label.pack()

        self.check_motion_button = tk.Button(master, text="Check Motion", command=self.check_motion)
        self.check_motion_button.pack()

    def check_motion(self):
        motion_detected = self.motion_sensor.detect_motion()
        self.motion_state_label.config(text=f"Motion Detected: {motion_detected}")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = MotionSensorGUI(root)
    root.mainloop()
