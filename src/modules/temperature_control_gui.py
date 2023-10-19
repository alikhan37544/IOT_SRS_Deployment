# temperature_control_gui.py

import tkinter as tk
from temperature_control import TemperatureControlSystem

class TemperatureControlGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Control System")

        self.temperature_system = TemperatureControlSystem()

        self.temperature_label = tk.Label(master, text="Temperature (°C):")
        self.temperature_label.pack()
        self.temperature_entry = tk.Entry(master)
        self.temperature_entry.pack()

        self.set_button = tk.Button(master, text="Set Temperature", command=self.set_temperature)
        self.set_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def set_temperature(self):
        try:
            temperature = float(self.temperature_entry.get())
            self.temperature_system.set_temperature(temperature)
            self.update_status(f"Temperature set to {temperature}°C")
        except ValueError:
            self.update_status("Invalid input. Please enter a valid temperature.")

    def update_status(self, message):
        self.status_label.config(text=message)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureControlGUI(root)
    root.mainloop()
