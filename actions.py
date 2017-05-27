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
    c.startTime = seconds()

    print "NOTE: {}\t{}".format(seconds(), c.startTime)

    u.wait_for_button()
    u.DEBUG()

    set_servo_position(c.SERVO_JOINT, c.JOINT_MID)
    set_servo_position(c.SERVO_BIN_ARM, c.arm_down)
    enable_servos()

    msleep(500)

    u.move_bin(c.arm_up)

    msleep(1000)

    exit(0)


def self_test():

    # x.rotate_spinner(1, 50)
    # u.wait_for_button()
    # x.rotate_spinner(1, -50)
    # exit(0)


    while not found_bump():
        pass
    print ("Good gyro")
    u.wait_for_button()
    enable_servos()
    x.drive_forever(80, 80)
    while not on_black_left() or not on_black_right():
        pass
    x.freeze_motors()
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_SPINNER_TEST)
    x.wait_for_someone_to_rotate()
    x.rotate_until_stalled(20)
    msleep(500)
    x.rotate_spinner(.056, -100)
    msleep(500)
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    msleep(500)
    x.rotate(15,60)
    msleep(1000)
    x.rotate(-15,60)
    print("DONE")
    u.wait_for_button()



def start():
    c.startTime = seconds()
    print "NOTE: {}\t{}".format(seconds(), c.startTime)
    u.move_servo(c.SERVO_JOINT, 0)
    enable_servo(0)


def leave_startbox():
    u.move_servo(c.SERVO_JOINT, c.JOINT_MID)
    find_black_line()
    x.pivot_left(-90, 60)
    x.drive_speed(-4, 100)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
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
    u.move_servo(c.SERVO_JOINT,c.JOINT_APPROACH)
    x.drive_speed(15,100, True)
    u.move_servo(c.SERVO_JOINT,c.JOINT_MID)
    x.drive_speed(25, 100)
    x.drive_condition(100, 100, found_bump, False)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_ALL_UP)

def found_bump():
    return gyro_y() > 200


def on_black_right():
    return analog(5) > 1000


def on_black_left():
    return analog(0) > 1000


def test_thingy():
    # u.move_servo(c.arm, 500, 2047)
    # u.move_servo(c.joint, 500)
    #
    # enable_servos()
    #
    # # x.drive_speed(5, 50)
    # #
    # # msleep(1000)
    #
    # u.move_servo(c.joint, 200, 5)
    #
    # msleep(500)
    #
    # u.move_bin(c.arm_all_up, 5)
    #
    # msleep(2000)
    #
    # exit(0)

    u.move_servo(c.SERVO_JOINT, 0)
    enable_servo(0)

    leave_startbox()
    drive_till_bump()

    x.drive_speed(4, 50)  # 4
    x.pivot_left(45, 50)
    x.rotate(-50, 50)
    x.drive_speed(-8, 100)

    u.wait_for_button()

    u.move_servo(c.SERVO_BIN_ARM, 500)
    u.move_servo(c.SERVO_JOINT, 850)

    enable_servos()

    msleep(1000)

    x.drive_speed(12, 30)

    u.move_servo(c.SERVO_JOINT, 300, 5)

    x.drive_speed(-30, 100)

    u.move_bin(c.ARM_ALL_UP)

    msleep(3000)


def get_bin():
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED)
    msleep(2000)
    x.drive_speed(3, 50)  # 4
    x.pivot_left(45, 50)
    x.rotate(-50, 50)
    x.drive_speed(-8, 100)

    # u.wait_for_button()

    u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    u.move_servo(c.SERVO_JOINT, c.JOINT_APPROACH)

    enable_servos()

    msleep(1000)

    x.drive_speed(12, 30)

    u.move_servo(c.SERVO_JOINT, c.JOINT_HOLD, 5)

    x.drive_speed(-30, 100)


def go_to_spinner():
    u.move_servo(c.SERVO_BIN_ARM,c.ARM_TUCKED)
    x.drive_speed(6, 50)
    x.pivot_right(100, 50)
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED)
    x.drive_speed(48, -100, True)
    x.drive_speed(-8, 40)
    x.drive_speed(3, 50)
    u.wait_for_button()
    x.rotate(-94, 50)
    x.drive_speed(-13, 50)
    x.drive_condition(80, 80, on_black_right, False)
    x.drive_speed(4, 75)
    u.wait_for_button()
    x.pivot_right(93, 50)
    x.drive_condition(80, 80, on_black_right, False)
    x.drive_speed(5, 50)
    u.move_servo(c.SERVO_JOINT, c.JOINT_ROTATE)
    u.wait_for_button()
    x.rotate(93, 50)
    u.move_servo(c.SERVO_JOINT, c.JOINT_APPROACH)
    disable_servos()
    x.drive_speed(3, 30)
    x.rotate_spinner(5, 50)
    u.DEBUG_WITH_WAIT()

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