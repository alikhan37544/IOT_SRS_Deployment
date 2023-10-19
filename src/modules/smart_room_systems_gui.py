import tkinter as tk
from access_control_gui import AccessControlGUI
from activity_alert_gui import ActivityAlertGUI
from appliance_control_gui import ApplianceControlGUI
from motion_sensor_gui import MotionSensorGUI
from temperature_control_gui import TemperatureControlGUI

class SmartRoomSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Smart Room System")
        self.master.configure(bg='#282c36')  # Set background color

        self.access_control_frame = tk.Frame(master, bg='#282c36')
        self.access_control_frame.pack(side=tk.LEFT, padx=20, pady=20)
        self.access_control_gui = AccessControlGUI(self.access_control_frame)

        self.activity_alert_frame = tk.Frame(master, bg='#282c36')
        self.activity_alert_frame.pack(side=tk.LEFT, padx=20, pady=20)
        self.activity_alert_gui = ActivityAlertGUI(self.activity_alert_frame)

        self.appliance_control_frame = tk.Frame(master, bg='#282c36')
        self.appliance_control_frame.pack(side=tk.LEFT, padx=20, pady=20)
        self.appliance_control_gui = ApplianceControlGUI(self.appliance_control_frame)

        self.motion_sensor_frame = tk.Frame(master, bg='#282c36')
        self.motion_sensor_frame.pack(side=tk.LEFT, padx=20, pady=20)
        self.motion_sensor_gui = MotionSensorGUI(self.motion_sensor_frame)

        self.temperature_control_frame = tk.Frame(master, bg='#282c36')
        self.temperature_control_frame.pack(side=tk.LEFT, padx=20, pady=20)
        self.temperature_control_gui = TemperatureControlGUI(self.temperature_control_frame)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='#282c36')  # Set background color
    app = SmartRoomSystemGUI(root)
    root.mainloop()
