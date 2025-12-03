from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

def loop():
  left, center_left, center, center_right, right = alvik.get_distance()
  # print(left, center_left, center, center_right, right)
  if center == 10:
    alvik.set_wheels_speed(0, 0)
  if center > 19:
    alvik.set_wheels_speed(120, 120)
  if 19 >= center > 18:
    alvik.set_wheels_speed(108, 108)
  if 18 >= center > 17:
    alvik.set_wheels_speed(108-12, 108-12)
  if 17 >= center > 16:
    alvik.set_wheels_speed(108-24, 108-24)
  if 16 >= center > 15:
    alvik.set_wheels_speed(108-36, 108-36)
  if 15 >= center > 14:
    alvik.set_wheels_speed(108-48, 108-48)
  if 14 >= center > 13:
    alvik.set_wheels_speed(108-60, 108-60)
  if 13 >= center > 12:
    alvik.set_wheels_speed(108-72, 108-72)
  if 12 >= center > 11:
    alvik.set_wheels_speed(108-84, 108-84)
  if 11 >= center > 10:
    alvik.set_wheels_speed(108-96, 108-96)
  if center == 10:
    alvik.set_wheels_speed(0, 0)
  if 9 <= center < 10:
    alvik.set_wheels_speed(-6*2, -6*2)
  if 8 <= center < 9:
    alvik.set_wheels_speed(-12*2, -12*2)
  if 7 <= center < 8:
    alvik.set_wheels_speed(-18*2, -18*2)
  if 6 <= center < 7:
    alvik.set_wheels_speed(-24*2, -24*2)
  if 5 <= center < 6:
    alvik.set_wheels_speed(-30*2, -30*2)
  if 4 <= center < 5:
    alvik.set_wheels_speed(-36*2, -36*2)
  if 3 <= center < 4:
    alvik.set_wheels_speed(-42*2, -42*2)
  if 2 <= center < 3:
    alvik.set_wheels_speed(-48*2, -48*2)
  if 1 <= center < 2:
    alvik.set_wheels_speed(-54*2, -54*2)
  if 0 <= center < 1:
    alvik.set_wheels_speed(-60*2, -60*2)
    

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)