# motion_sensor.py

import grovepi
import random

class MotionSensor:
    def __init__(self, motion_sensor_port=2, gui_mode=False):
        self.motion_sensor_port = motion_sensor_port  # Port D2 on GrovePi
        grovepi.pinMode(self.motion_sensor_port, "INPUT")
        self.gui_mode = gui_mode
        self.motion_detected = False

    def detect_motion(self):
        if self.gui_mode:
            # Simulate motion detection in GUI mode
            return self.simulate_motion_detection()
        else:
            # Read motion sensor data from Grove Pi in RasPi mode
            return self.read_grovepi_motion_sensor()

    def simulate_motion_detection(self):
        # Simulate motion detection (for GUI mode)
        return random.choice([True, False])

    def read_grovepi_motion_sensor(self):
        # Read motion sensor data from Grove Pi (for RasPi mode)
        try:
            motion_detected = grovepi.digitalRead(self.motion_sensor_port)
            return motion_detected == 1
        except Exception as e:
            print("Error reading motion sensor:", str(e))
            return False

    def set_gui_mode(self, gui_mode):
        self.gui_mode = gui_mode

    def get_motion_state(self):
        return self.motion_detected
