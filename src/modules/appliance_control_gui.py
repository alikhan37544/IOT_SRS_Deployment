# appliance_control_gui.py

import tkinter as tk
from appliance_control import ApplianceController

class ApplianceControlGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Appliance Controller Simulator")

        self.appliance_controller = ApplianceController()

        self.appliance_button = tk.Button(master, text="Toggle Appliance", command=self.toggle_appliance)
        self.appliance_button.pack()

    def toggle_appliance(self):
        current_state = self.appliance_controller.get_appliance_state()
        if current_state:
            self.appliance_controller.turn_off_appliance()
        else:
            self.appliance_controller.turn_on_appliance()

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplianceControlGUI(root)
    root.mainloop()
