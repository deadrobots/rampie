from wallaby import *
import utils as u
import motorsPlusPlus as x
import constants as c


def init():
    u.move_servo(c.SERVO_BIN_ARM, c.BIN_ARM_IN, 10)
    enable_servos()
    # this is where it stops at the top
    msleep(2500)
    set_servo_position(c.SERVO_BIN_ARM, c.BIN_ARM_DELIVER)
    x.linefollow_distance(23.46)
    u.DEBUG_WITH_WAIT()


def find_black_line():
    print "In one"
    while not on_black_left() and not on_black_right():
        print "while"
        x.drive_forever(60,60)
    if on_black_left():
        print "if"
        x.drive_condition(-40, 25, on_black_right, False)
    elif on_black_right():
        print "elif"
        x.drive_condition(25,-40, on_black_left, False)


def drive_till_bump():
    x.rotate(-90, 50)
    x.drive_speed(12, 100)
    x.drive_condition(100, 100, find_bump)


def find_bump():
    return gyro_y() < 200


def on_black_right():
    return analog(5) > 1000


def on_black_left():
    return analog(0) > 1000


def get_bin():
    x.drive_speed(4,50)
    x.pivot_left(45,50)
    x.rotate(-50,50)
    msleep(2000)


def go_to_ramp():
    x.drive_speed(-3,50)
    x.rotate(-95,50)
    u.move_servo(c.SERVO_BIN_ARM, c.BIN_ARM_DRIVE, 10)
    while not on_black_left() and not on_black_right():
        x.drive_forever(60,60)
    if on_black_left():
        x.drive_condition(-40, 25, on_black_right, False)
    elif on_black_right():
        x.drive_condition(25,-40, on_black_left, False)
    x.drive_speed(6, 70)
    u.move_servo(c.SERVO_BIN_ARM, c.BIN_CLAW_CASTER, 10)
    x.rotate(-97, 50)
    x.drive_speed(-3,60)
    x.rotate(-93,50)
    x.drive_speed(-15,60)
    x.drive_speed(6,80)
    x.rotate(95,50)
    x.drive_speed(-20, 80)
    u.move_servo(c.SERVO_BIN_ARM, c.BIN_UP_RAMP)
    x.drive_speed(5,50)
    x.rotate(-91.5, 50)


def up_ramp():
    set_servo_position(c.SERVO_BIN_ARM, c.BIN_ARM_STRAIGHT)
    enable_servos()
    u.wait_for_button()
    x.drive_speed(22, 100)
    msleep(3000)
    x.drive_speed(2, 75)
    while gyro_y() > -350 and gyro_y() > -350:
        print(gyro_y())
        if analog(0) < 1000:
            x.drive_forever(60, 100)
        else:
            x.drive_forever(100, 80)
    print(gyro_x())
    print(gyro_y())
    x.drive_speed(6, 100)