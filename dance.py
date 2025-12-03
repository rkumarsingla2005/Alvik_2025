# IMPORTING NECESSARY LIBRARIES

from arduino import *
from arduino_alvik import ArduinoAlvik



#INITIALIZING ALVIK

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(500)

def loop():
  alvik.set_wheels_speed(60, -60)
  delay(3000)
  alvik.set_wheels_speed(60, 0)
  delay(983)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)
  