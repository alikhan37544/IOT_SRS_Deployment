# smart_room_system.py

from access_control import AccessControlSystem
from activity_alert import ActivityAlertSystem, AlertSubscriber
from appliance_control import ApplianceControlSystem
from motion_sensor import MotionSensor
from temperature_control import TemperatureControlSystem

class SmartRoomSystem:
    def __init__(self):
        self.access_system = AccessControlSystem()
        self.activity_alert_system = ActivityAlertSystem()
        self.appliance_system = ApplianceControlSystem()
        self.motion_sensor = MotionSensor()
        self.temperature_system = TemperatureControlSystem()

        # Example subscribers for activity alerts
        self.subscriber1 = AlertSubscriber("Security Room")
        self.subscriber2 = AlertSubscriber("Admin Office")
        self.activity_alert_system.subscribe(self.subscriber1)
        self.activity_alert_system.subscribe(self.subscriber2)

    def run_cli(self):
        print("Welcome to Smart Room System CLI!")
        while True:
            print("\nMenu:")
            print("1. Access Control")
            print("2. Activity Alert System")
            print("3. Appliance Control")
            print("4. Motion Sensor")
            print("5. Temperature Control")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                # Implement access control logic here
                pass
            elif choice == "2":
                # Implement activity alert system logic here
                pass
            elif choice == "3":
                # Implement appliance control logic here
                pass
            elif choice == "4":
                # Implement motion sensor logic here
                pass
            elif choice == "5":
                # Implement temperature control logic here
                pass
            elif choice == "0":
                print("Exiting Smart Room System CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    smart_room_system = SmartRoomSystem()
    smart_room_system.run_cli()
