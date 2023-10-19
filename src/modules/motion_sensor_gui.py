# motion_sensor_gui.py

from motion_sensor import MotionSensor
import tkinter as tk
import random

class MotionSensorGUI:
    def __init__(self, master, motion_sensor, gui_mode=True):
        self.master = master
        self.master.title("Motion Sensor Simulator")
        self.motion_sensor = motion_sensor
        self.motion_sensor.set_gui_mode(gui_mode)

        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()

        self.update_canvas()

        self.motion_button = tk.Button(master, text="Toggle Motion", command=self.toggle_motion)
        self.motion_button.pack()

    def toggle_motion(self):
        current_state = self.motion_sensor.detect_motion()
        print("Motion Detected:", current_state)
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        motion_state = self.motion_sensor.get_motion_state()
        color = "red" if motion_state else "green"
        self.canvas.create_oval(50, 50, 150, 150, fill=color)

# Example usage
if __name__ == "__main__":
    # Port D2 on GrovePi for the motion sensor
    motion_sensor_port = 2
    motion_sensor = MotionSensor(motion_sensor_port)

    # GUI mode is set to True here, you can change it based on your requirements
    root = tk.Tk()
    app = MotionSensorGUI(root, motion_sensor, gui_mode=True)
    root.mainloop()
