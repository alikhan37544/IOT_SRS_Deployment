# appliance_control.py

class ApplianceController:
    def __init__(self):
        self.appliance_state = False

    def turn_on_appliance(self):
        self.appliance_state = True
        print("Appliance turned ON")

    def turn_off_appliance(self):
        self.appliance_state = False
        print("Appliance turned OFF")

    def get_appliance_state(self):
        return self.appliance_state
