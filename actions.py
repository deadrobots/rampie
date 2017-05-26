from wallaby import *
import utils as u
import motorsPlusPlus as x
import constants as c


def init():
    # u.move_servo(c.SERVO_BIN_ARM, c.BIN_ARM_IN, 10)
    enable_servos()
    # this is where it stops at the top
    msleep(2500)
    # set_servo_position(c.SERVO_BIN_ARM, c.BIN_ARM_DELIVER)
    x.linefollow_distance(23.46)
    u.DEBUG_WITH_WAIT()


def test():

    u.wait_for_button()
    u.DEBUG()

    set_servo_position(c.joint, c.joint_mid)
    set_servo_position(c.arm, c.arm_down)
    enable_servos()

    msleep(500)

    u.move_bin(c.arm_up)

    msleep(1000)

    exit(0)


def start():
    enable_servos()
    u.move_servo(c.arm, c.arm_up)
    u.move_servo(c.joint, c.joint_tucked)


def leave_startbox():
    find_black_line()
    x.pivot_left(-90, 60)
    x.drive_speed(-4, 100)
    u.move_servo(c.arm, c.arm_tucked)
    find_black_line()
    x.drive_speed(8, 80)
    x.pivot_right(-90, 60)
    x.drive_speed(-5, 100)


def find_black_line():
    print "In one"
    x.drive_forever(60, 60)
    while not on_black_left() and not on_black_right():
        print "while"
    # if on_black_left():
    #     print "if"
    #     x.drive_condition(-40, 25, on_black_right, False)
    # elif on_black_right():
    #     print "elif"
    #     x.drive_condition(25,-40, on_black_left, False)
    x.freeze_motors()


def drive_till_bump():
    x.drive_speed(40, 100, True)
    x.drive_condition(100, 100, find_bump)


def find_bump():
    return gyro_y() < 200


def on_black_right():
    return analog(5) > 1000


def on_black_left():
    return analog(0) > 1000


def get_bin():
    x.drive_speed(3,50) # 4
    # u.move_servo(c.arm, c.arm_all_up)
    x.pivot_left(45,50)
    x.rotate(-50,50)
    # msleep(2000)
    # x.drive_speed(-11, 100)

    u.move_servo(c.arm, c.arm_half_tucked)
    u.move_servo(c.joint, c.joint_mid, 100)
    u.move_servo(c.claw, c.claw_open, 100)
    u.move_servo(c.arm, c.arm_down, 2)

    # x.drive_speed(3, 100)
    #
    # x.drive_speed(6, 50, True)
    x.drive_forever(30, 30)
    msleep(2000)
    u.move_servo(c.claw, c.claw_close)
    msleep(100)
    x.freeze_motors()

    x.drive_speed(-30, 99)

    u.move_bin(c.arm_all_up)

    msleep(3000)
    x.drive_speed(10,100)


def go_to_spinner():
    x.rotate(105, 30)
    x.drive_speed(-51, 100)
    u.DEBUG()
    x.drive_speed(7,-100)
    x.pivot_right(100,100)
    x.drive_speed(35,-100)


def go_to_ramp():
    x.drive_speed(-6,50)
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