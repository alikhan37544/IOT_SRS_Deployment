# grovepi_motion_sensor.py

import grovepi

# Port D2 on GrovePi for the motion sensor
motion_sensor_port = 2
grovepi.pinMode(motion_sensor_port, "INPUT")

def read_motion_sensor():
    try:
        motion_detected = grovepi.digitalRead(motion_sensor_port)
        return motion_detected == 1
    except Exception as e:
        print("Error reading motion sensor:", str(e))
        return False

# Example usage
if __name__ == "__main__":
    motion_detected = read_motion_sensor()
    print("Motion Detected:", motion_detected)
