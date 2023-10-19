# appliance_control.py

class ApplianceControlSystem:
    def __init__(self):
        self.appliances = {}

    def add_appliance(self, name, status=False):
        self.appliances[name] = status

    def toggle_appliance(self, name):
        if name in self.appliances:
            self.appliances[name] = not self.appliances[name]
            print(f"{name} is {'On' if self.appliances[name] else 'Off'}")
        else:
            print(f"Appliance {name} not found.")

    def get_appliance_status(self, name):
        return self.appliances.get(name, "Appliance not found")

# Example usage
if __name__ == "__main__":
    appliance_system = ApplianceControlSystem()

    # Adding appliances
    appliance_system.add_appliance("Light", False)
    appliance_system.add_appliance("Fan", True)

    # Toggling appliances
    appliance_system.toggle_appliance("Light")
    appliance_system.toggle_appliance("Fan")

    # Checking appliance status
    print(appliance_system.get_appliance_status("Light"))
