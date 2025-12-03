from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(500)

def loop():
  alvik.set_wheels_speed(30, 0)
  delay(5900)
  alvik.set_wheels_speed(0, 0)
  delay(500)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)