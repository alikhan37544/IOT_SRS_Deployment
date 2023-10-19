# access_control_gui.py

import tkinter as tk
from access_control import AccessControlSystem

class AccessControlGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Access Control System")

        self.access_system = AccessControlSystem()

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.access_button = tk.Button(master, text="Check Access", command=self.check_access)
        self.access_button.pack()

        self.access_result_label = tk.Label(master, text="")
        self.access_result_label.pack()

    def check_access(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.access_system.grant_access(username, password)  # Calls the grant_access method from AccessControlSystem
        # Display the access result
        result = f"Access granted for {username}" if username in self.access_system.users and self.access_system.users[username] == password else f"Access denied for {username}"
        self.access_result_label.config(text=result)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = AccessControlGUI(root)
    root.mainloop()
