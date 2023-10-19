# motion_sensor.py

import random

class MotionSensor:
    def __init__(self, gui_mode=False):
        self.gui_mode = gui_mode
        self.motion_detected = False

    def detect_motion(self):
        if self.gui_mode:
            return self.simulate_motion_detection()
        else:
            return self.read_motion_sensor()

    def simulate_motion_detection(self):
        return random.choice([True, False])

    def read_motion_sensor(self):
        # Logic to read motion sensor data (not implemented in this example)
        # Return True if motion detected, False otherwise
        pass

    def set_gui_mode(self, gui_mode):
        self.gui_mode = gui_mode

    def get_motion_state(self):
        return self.motion_detected
