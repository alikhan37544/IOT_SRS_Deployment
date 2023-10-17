# motion_sensor_gui.py

import tkinter as tk
from motion_sensor import MotionSensor

class MotionSensorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Motion Sensor Simulator")

        self.motion_sensor = MotionSensor()

        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()

        self.update_canvas()

        self.motion_button = tk.Button(master, text="Toggle Motion", command=self.toggle_motion)
        self.motion_button.pack()

    def toggle_motion(self):
        current_state = self.motion_sensor.get_motion_state()
        new_state = not current_state
        self.motion_sensor.set_motion_state(new_state)
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        motion_state = self.motion_sensor.get_motion_state()
        color = "red" if motion_state else "green"
        self.canvas.create_oval(50, 50, 150, 150, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = MotionSensorGUI(root)
    root.mainloop()
