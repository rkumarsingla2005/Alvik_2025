from arduino import *
from arduino_alvik import ArduinoAlvik
import math

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

def loop():
  roll, pitch, yaw = alvik.get_orientation()
  a = math.ceil(roll)
  b = math.ceil(pitch)
  c = math.ceil(yaw)

  print(a, b, c)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)