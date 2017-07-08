from wallaby import *
import utils as u
import motorsPlusPlus as x
import constants as c
from logger import log as display


def test_ramp():

    x.drive_speed(100, 100)
    u.DEBUG()

    enable_servos()
    u.move_servo(c.DEPLOYABLE_WHEELS, c.WHEELS_DEPLOYED)
    u.move_bin(c.ARM_SWING)
    x.drive_speed(12, 100)
    start_time = seconds()
    x.drive_speed(5, 100)
    while gyro_y() < 100 or seconds() < start_time + 2:
        if u.on_black_front():
            x.drive_forever(70, 100)
        else:
            x.drive_forever(100, 70)
        msleep(10)
    x.drive_speed(4, 100)
    x.pivot_left_condition(30, u.on_black_front, False)


def alt_init():
    u.move_servo(c.SERVO_JOINT, c.JOINT_MID, 2047)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED, 2047)
    enable_servos()
    u.wait_for_button()
    # u.move_bin(c.ARM_SWING)
    # u.move_bin(c.ARM_ALL_UP)
    x.drive_speed(70, 100)
    # x.rotate(180, 50)
    # u.wait_for_button()
    # go_up_ramp()

def select():
    end = seconds() + 3
    exit_loop = True
    state = 0
    changed = False
    begin = False
    for setting in range(0, 8):
        if digital(setting):
            begin = True
    if begin:
        display("Starting selection")
        while not exit_loop or seconds() < end:
            for setting in range(0, 8):
                if digital(setting) and setting != state:
                    state = setting
                    changed = True
                    while digital(setting):
                        pass
            if state != 0:
                exit_loop = False
                if changed:
                    display("SELECTION: {}".format(state))
                    changed = False
            if right_button():
                while right_button():
                    pass
                display("Running table setting {}".format(state))
                msleep(300)
                exit_loop = True
                end = 0
        display("Ended selection")


def select2():
    selection = 0
    if digital(0):
        display("Started selection\n")
        display("Set to: {}".format(selection))
        while digital(0):
            pass
        while not right_button():
            if digital(0):
                while digital(0):
                    pass
                selection += 1
                display("Set to: {}".format(selection))
        display("\n Ended selection\n")


def init():
    display("\nFunction: init\n")
    if c.IS_CLONE:
        display("I AM CLONE")
    else:
        display("I AM PRIME")
    # enable_servos()
    # msleep(2500)
    # x.linefollow_distance(23.46)
    # u.DEBUG_WITH_WAIT()


def self_test():
    display("\nFunction: self_test\n")
    display("Click left button to use botguy hitter else hit right")
    while not right_button() and not left_button():
        pass
    if right_button():
        c.HIT_BOTGUY = False
        display("wont hit botguy")
    elif left_button():
        c.HIT_BOTGUY = True
        display("will hit botguy")
    display("DONE SETTING")
    if u.on_black_front() or u.on_black_back():
        display("Something is wrong with the tophats!")
        display("LTOPHAT: {}\tRTOPHAT: {}".format(u.on_black_front(), u.on_black_back()))
        exit(1)
    while not u.found_bump():
        pass
    display("Good gyro")
    u.wait_for_button()
    enable_servos()
    x.drive_forever(80, 80)
    x.drive_condition(80, 80, u.on_black_front, False)
    msleep(500)
    x.drive_condition(80, 80, u.on_black_back, False)
    x.freeze_motors()
    u.move_servo(c.SERVO_JOINT, c.JOINT_MID)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_SPINNER_TEST)
    x.wait_for_someone_to_rotate()
    u.wait_for_button()
    x.rotate_until_stalled(20)
    msleep(500)
    x.rotate_spinner(.06, -30)
    msleep(500)
    x.set_spinner_safe()
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    u.move_servo(c.SERVO_BOT_GUY_HITTER, c.HITTER_OUT)
    u.move_servo(c.SERVO_BOT_GUY_HITTER, c.HITTER_IN)
    msleep(500)
    x.rotate(15,60)
    msleep(1000)
    x.rotate(-15,60)

    display("DONE")


def start():
    display("\nFunction: start\n")
    u.wait_4_light(ignore=False)
    if c.IS_CLONE:
        msleep(2500)
    else:
        msleep(2000)
    shut_down_in(119.75)
    c.startTime = seconds()
    display("NOTE: {}\t{}".format(seconds(), c.startTime))
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED)
    enable_servo(c.SERVO_JOINT)


def leave_startbox():
    display("\nFunction: leave_startbox\n")
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    x.drive_condition(80, 80, u.on_black_front, False)
    x.drive_speed(-4, 60)
    if c.IS_CLONE:
        x.rotate(-92, 70)
    else:
        x.rotate(-96, 70)
    x.drive_speed(-34, 100)
    x.drive_condition(80, 80, u.on_black_front, False)
    x.drive_speed(1, 80)
    x.rotate(92, 60)
    x.drive_speed(-7, 85)


def drive_till_bump():
    display("\nFunction: drive_till_bump\n")
    if c.IS_CLONE:
        x.drive_speed(41, 100, True)
    else:
        x.drive_speed(42, 100, True)


def get_bin():
    display("\nFunction: get_bin\n")
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED, 100)
    if c.IS_CLONE:
        x.rotate(-86, 50)
    else:
        x.rotate(-90, 50)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    u.move_servo(c.SERVO_JOINT, c.JOINT_SWING)
    msleep(250)
    if c.IS_CLONE:
        x.drive_speed(12, 70)
    else:
        x.drive_speed(10, 70)
    u.move_servo(c.SERVO_JOINT, c.JOINT_SWING)
    if c.IS_CLONE:
        u.move_bin(c.ARM_DRIVE,5)
    else:
        u.move_bin(c.ARM_SWING, 5)
    u.move_servo(c.SERVO_JOINT, c.JOINT_PARALLEL, 5)
    u.move_bin(c.ARM_APPROACH, 5)
    u.move_servo(c.SERVO_JOINT, c.JOINT_ROTATE, 5)
    # x.drive_speed(-20, 100)

    x.drive_speed(-16, 100)
    x.drive_speed(-4, 50)
    if c.HIT_BOTGUY:
        u.move_servo(c.SERVO_BOT_GUY_HITTER, c.HITTER_OUT, 100)
        x.pivot_right(30,75)
        x.pivot_right(-30, 75)
        u.move_servo(c.SERVO_BOT_GUY_HITTER, c.HITTER_IN, 100)
    u.move_bin(c.ARM_SPINNER_TEST)

def go_to_spinner():
    display("\nFunction: go_to_spinner\n")
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED, 5)
    if c.IS_CLONE:
        x.drive_speed(8, 100)
    else:
        x.drive_speed(11, 100)
    if c.IS_CLONE:
        x.pivot_left(-90, 70)
    else:
        x.pivot_left(-88, 70)
    x.drive_speed(22, -100, True)
    x.pivot_left(-32, 50)
    x.drive_speed(-11, 80)
    x.pivot_right(-32, 50)
    x.drive_speed(-3, 70)
    x.drive_condition(50, 50, u.on_black_front, False)
    if c.IS_CLONE:
        x.rotate(90, 35)
    else:
        x.rotate(98, 35)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    u.move_servo(c.SERVO_JOINT, c.JOINT_PARALLEL)
    x.drive_condition(80, 80, u.on_black_front, False)
    x.drive_condition(50, 50, u.on_black_front, True)
    x.rotate_spinner(.25, 80)
    x.drive_speed(5, 60)
    u.move_servo(c.SERVO_JOINT, c.JOINT_GROUND)
    x.rotate_spinner(4, -70)
    x.rotate_to_safe(50)


def go_to_ramp():
    display("\nFunction: go_to_ramp\n")
    u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_ON)
    u.move_servo(c.SERVO_JOINT, c.JOINT_ARM_TILT)
    if c.IS_CLONE:
        x.rotate(-5, 50)
    else:
        x.rotate(-5, 50)
    x.drive_forever(-50, -50)
    u.move_bin(c.ARM_TILT, 5)
    x.drive_speed(-10, 100)
    x.rotate(5, 65)
    u.move_servo(c.SERVO_JOINT, c.JOINT_HOLD, 5)
    u.move_bin(c.ARM_TUCKED, 5)
    msleep(100)
    x.drive_speed(-7, 100)
    x.drive_speed(-6, 75)
    x.drive_speed(2, 75)
    x.pivot_right(-90, 60)
    u.move_servo(c.SERVO_JOINT, c.JOINT_MID)


def go_up_ramp():
    display("\nFunction: go_up_ramp\n")
    u.move_bin(c.ARM_SWING)
    x.drive_speed(12, 100)
    start_time = seconds()
    x.drive_speed(5, 100)

    if c.IS_CLONE:
        while gyro_y() < 100 or seconds() < start_time + 2:
            if u.on_black_front():
                x.drive_forever(50, 100)
            else:
                x.drive_forever(100, 70)
            msleep(10)
    else:
        while gyro_y() < 100 or seconds() < start_time + 2:
            if u.on_black_front():
                x.drive_forever(50, 100)
            else:
                x.drive_forever(100, 50)
            msleep(10)
    x.drive_speed(8, 100)
    u.move_servo(c.SERVO_JOINT, c.JOINT_GROUND)

    # u.wait_for_button()
    print("1")
    x.pivot_left_condition(30, u.on_black_front, False)

    # u.wait_for_button()
    print("2")
    # if u.on_black_back():
    x.pivot_right_condition(30, u.on_black_back)
        # x.pivot_right(35, 30)

    # u.wait_for_button()
    print("3")
    x.pivot_right_condition(30, u.on_black_back, False)
    # u.wait_for_button()
    print("4")
    x.pivot_left_condition(30, u.on_black_front, False)
    # u.wait_for_button()
    print("5")

    u.move_bin(c.ARM_ALL_UP)
    msleep(500)


def go_and_score_the_bin():
    display("\nFunction: go_and_score_the_bin\n")
    u.move_servo(c.SERVO_JOINT, c.JOINT_DELIVER,4)
    msleep(500)
    u.move_servo(c.SERVO_BOT_GUY_HITTER, c.HITTER_OUT, 100)
    # x.linefollow_distance(28, 50, 70)
    x.linefollow_distance(20, 50, 70, 5)
    x.pivot_right(-32.5, 50)

    # x.drive_speed(-2, 50)
    # x.rotate(-10, 50)
    # x.drive_speed(2.5, 50)
    # x.pivot_right(40, 50)
    # x.drive_speed(2.5, 50)
    # u.wait_for_button()

    if not c.IS_CLONE:
        x.drive_speed(1, 50)
    disable_servo(c.SERVO_JOINT)
    msleep(500)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_MAX)
    msleep(500)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_HIT, 20)
    msleep(300)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_MAX, 20)
    x.drive_speed(1, 50)
    x.pivot_right(30, 50)



