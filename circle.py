# IMPORTING NECESSARY LIBRARIES

from arduino import *
from arduino_alvik import ArduinoAlvik
import math


#INITIALIZING ALVIK

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(500)

def loop():
  alvik.set_wheels_speed(60, 30)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)