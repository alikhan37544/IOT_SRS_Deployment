# temperature_control.py

class TemperatureControlSystem:
    def __init__(self):
        self.temperature = 25  # Default temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature set to {temperature}°C")

    def get_temperature(self):
        return self.temperature

# Example usage
if __name__ == "__main__":
    temperature_system = TemperatureControlSystem()

    # Setting temperature
    temperature_system.set_temperature(22)

    # Getting current temperature
    current_temperature = temperature_system.get_temperature()
    print(f"Current Temperature: {current_temperature}°C")
