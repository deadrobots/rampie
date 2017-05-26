'''
Created on Jan 3, 2016
@author: graysonelias
'''

'''
This module provides some of our standard methods.
'''

import constants as c

from wallaby import ao
from wallaby import msleep
from wallaby import digital
from wallaby import seconds
from wallaby import freeze
from wallaby import set_servo_position
from wallaby import get_servo_position
from wallaby import analog

# Servo Constants
DELAY = 10
# Loop break timers #
time = 0  # This represents how long to wait before breaking a loop.


#Causes the robot to stop until the right button is pressed
def wait_for_button():
    print "Press Button..."
    while not digital(c.RIGHT_BUTTON):
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)


#Causes the robot to stop
def DEBUG():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    ao()
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime
    exit(0)


#Causes the robot to stop and hold its position for 5 seconds
def DEBUG_WITH_WAIT():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    ao()
    msleep(5000)
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime
    exit(0)


#Checks to see if all of the servos, motors, and sensors are working properly
def start_up_test():
    DEBUG()
# Servo Control #
# Moves a servo with increment "speed".


def move_servo(servo, endPos, speed=10):
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if speed == 0:
        speed = 2047
    if endPos >= 2048:
        print "Programmer Error"
    if endPos < 0:
        print "Programmer Error"
    if now > endPos:
        speed = -speed
    for i in range(int(now), int(endPos), int(speed)):
        set_servo_position(servo, i)
        msleep(DELAY)
    set_servo_position(servo, endPos)
    msleep(DELAY)

# Moves a servo over a specific time.


def move_servo_timed(servo, endPos, time):
    if time == 0:
        speed = 2047
    else:
        speed = abs((DELAY * (get_servo_position(servo) - endPos)) / time)
    move_servo(servo, endPos, speed)


# Sets wait time in seconds before breaking a loop.
def set_wait(DELAY):
    global time
    time = seconds() + DELAY

# Used to break a loop after using "setWait". An example would be: setWiat(10) | while true and getWait(): do something().


def get_wait():
    return seconds() < time


def wait_4_light():
    while not calibrate(c.STARTLIGHT):
        pass
    wait_4(c.STARTLIGHT)

from wallaby import left_button, right_button


def calibrate(port):
    print "Press LEFT button with light on"
    while not left_button():
        pass
    while left_button():
        pass
    lightOn = analog(port)
    print "On value =", lightOn
    if lightOn > 200:
        print "Bad calibration"
        return False
    msleep(1000)
    print "Press RIGHT button with light off"
    while not right_button():
        pass
    while right_button():
        pass
    lightOff = analog(port)
    print "Off value =", lightOff
    if lightOff < 3000:
        print "Bad calibration"
        return False

    if (lightOff - lightOn) < 2000:
        print "Bad calibration"
        return False
    c.startLightThresh = (lightOff - lightOn) / 2
    print "Good calibration! ", c.startLightThresh
    return True


def wait_4(port):
    print "waiting for light!! "
    if c.seeding:
        print("SEEDING")
    else:
        print("HEAD TO HEAD")
    while analog(port) > c.startLightThresh:
        pass


def move_bin(armEnd, speed=10): # 1263
    joint_start = get_servo_position(c.joint) # 1750
    arm_start = get_servo_position(c.arm) # 700
    delta = armEnd - arm_start # 563
    for shift in range(0, delta, speed):
        set_servo_position(c.arm, arm_start + shift)
        set_servo_position(c.joint, joint_start + shift)

        print "{}\t{}".format(get_servo_position(c.joint), get_servo_position(c.arm))

        msleep(DELAY)
    set_servo_position(c.arm, arm_start + delta)
    set_servo_position(c.joint, joint_start + delta)