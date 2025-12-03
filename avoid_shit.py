from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

def loop():
  alvik.set_wheels_speed(60, 60)
  left, center_left, center, center_right, right = alvik.get_distance()
  if center < 10:
    alvik.set_wheels_speed(0, 0)
    delay(1000)
    alvik.set_wheels_speed(60,-60)
    delay(850)
    alvik.set_wheels_speed(0, 0)
    delay(1000)
    alvik.set_wheels_speed(60, 60)
    delay(1200)
    alvik.set_wheels_speed(0, 0)
    delay(1000)
    alvik.set_wheels_speed(-60,60)
    delay(850)
    alvik.set_wheels_speed(0, 0)
    delay(1000)
    alvik.set_wheels_speed(60, 60)
    delay(3000)
    alvik.set_wheels_speed(0, 0)
    delay(1000)
    alvik.set_wheels_speed(-60,60)
    delay(850)
    alvik.set_wheels_speed(0, 0)
    delay(1000)
    alvik.set_wheels_speed(60, 60)
    delay(1200)
    alvik.set_wheels_speed(0, 0)
    delay(1000)
    alvik.set_wheels_speed(60,-60)
    delay(850)
    alvik.set_wheels_speed(0, 0)
    delay(1000)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)
    


    
    