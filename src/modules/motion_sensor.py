# motion_sensor.py

import random

class MotionSensor:
    def __init__(self):
        self.motion_detected = False

    def detect_motion(self):
        # Simulate motion detection (True) or no motion (False)
        self.motion_detected = random.choice([True, False])
        return self.motion_detected

    def set_motion_state(self, state):
        # Manually set motion detection state
        self.motion_detected = state

    def get_motion_state(self):
        return self.motion_detected
