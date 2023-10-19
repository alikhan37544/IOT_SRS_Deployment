# appliance_control_gui.py

import tkinter as tk
from appliance_control import ApplianceControlSystem

class ApplianceControlGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Appliance Control System")

        self.appliance_system = ApplianceControlSystem()

        self.appliance_name_label = tk.Label(master, text="Appliance Name:")
        self.appliance_name_label.pack()
        self.appliance_name_entry = tk.Entry(master)
        self.appliance_name_entry.pack()

        self.add_button = tk.Button(master, text="Add Appliance", command=self.add_appliance)
        self.add_button.pack()

        self.toggle_button = tk.Button(master, text="Toggle Appliance", command=self.toggle_appliance)
        self.toggle_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def add_appliance(self):
        appliance_name = self.appliance_name_entry.get()
        self.appliance_system.add_appliance(appliance_name)
        print(f"Appliance {appliance_name} added.")

    def toggle_appliance(self):
        appliance_name = self.appliance_name_entry.get()
        status = self.appliance_system.get_appliance_status(appliance_name)
        if status != "Appliance not found":
            self.appliance_system.toggle_appliance(appliance_name)
            self.update_status(f"{appliance_name} is {'On' if status else 'Off'}")
        else:
            self.update_status(f"Appliance {appliance_name} not found.")

    def update_status(self, message):
        self.status_label.config(text=message)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = ApplianceControlGUI(root)
    root.mainloop()
