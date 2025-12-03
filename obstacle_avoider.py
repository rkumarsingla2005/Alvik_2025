from arduino_alvik import ArduinoAlvik
import time

# Initialize Alvik
alvik = ArduinoAlvik()
alvik.begin()

while True:
    # Moves servo 0
    alvik.set_servo_positions(0,0)
    time.sleep(2)
    alvik.set_servo_positions(90,0)
    time.sleep(2)
    alvik.set_servo_positions(180,0)
    time.sleep(2)
    alvik.set_servo_positions(90,0)
    time.sleep(2)
    # Moves servo 1
    alvik.set_servo_positions(0,1)
    time.sleep(2)
    alvik.set_servo_positions(90,1)
    time.sleep(2)
    alvik.set_servo_positions(180,1)
    time.sleep(2)
    alvik.set_servo_positions(90,1)
    time.sleep(2)