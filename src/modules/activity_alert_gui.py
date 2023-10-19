# activity_alert_gui.py

import tkinter as tk
from activity_alert import ActivityAlertSystem, AlertSubscriber

class ActivityAlertGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Activity Alert System")

        self.activity_alert_system = ActivityAlertSystem()

        self.subscriber_name_label = tk.Label(master, text="Subscriber Name:")
        self.subscriber_name_label.pack()
        self.subscriber_name_entry = tk.Entry(master)
        self.subscriber_name_entry.pack()

        self.subscribe_button = tk.Button(master, text="Subscribe", command=self.subscribe)
        self.subscribe_button.pack()

        self.alert_label = tk.Label(master, text="Alert Message:")
        self.alert_label.pack()
        self.alert_entry = tk.Entry(master)
        self.alert_entry.pack()

        self.notify_button = tk.Button(master, text="Notify Subscribers", command=self.notify_subscribers)
        self.notify_button.pack()

    def subscribe(self):
        subscriber_name = self.subscriber_name_entry.get()
        subscriber = AlertSubscriber(subscriber_name)
        self.activity_alert_system.subscribe(subscriber)
        print(f"{subscriber_name} subscribed to alerts.")

    def notify_subscribers(self):
        alert_message = self.alert_entry.get()
        self.activity_alert_system.notify_subscribers(alert_message)
        print(f"Alert sent: {alert_message}")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = ActivityAlertGUI(root)
    root.mainloop()
