from wallaby import *
import utils as u
import motorsPlusPlus as x
import constants as c
from logger import log as display


def init():

    if c.IS_CLONE:
        display("I AM CLONE")
    else:
        display("I AM PRIME")
    enable_servos()
    msleep(2500)
    x.linefollow_distance(23.46)
    u.DEBUG_WITH_WAIT()


def test():

    u.wait_for_button()
    x.set_spinner_safe()
    x.rotate_spinner(6, 100)
    exit(0)

    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED, 1000)
    u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_ON, 1000)
    enable_servos()
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_ON)
    u.wait_for_button()
    u.move_bin(c.ARM_ALL_UP)
    u.wait_for_button()
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_ON)
    u.wait_for_button()
    u.move_bin(c.ARM_ALL_UP, 2)
    u.wait_for_button()


def self_test():
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
    msleep(500)
    x.rotate(15,60)
    msleep(1000)
    x.rotate(-15,60)
    display("DONE")
    u.wait_for_button()


def start():
    c.startTime = seconds()
    display("NOTE: {}\t{}".format(seconds(), c.startTime))
    u.move_servo(c.SERVO_JOINT, 0)
    enable_servo(0)


def leave_startbox():
    u.move_servo(c.SERVO_JOINT, c.JOINT_MID)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    x.drive_condition(80, 80, u.on_black_front, False)
    x.drive_speed(-4, 50)
    x.rotate(-96, 50)
    x.drive_speed(-34, 100)
    x.drive_condition(80, 80, u.on_black_front, False)
    x.rotate(92, 60)
    x.drive_speed(-5, 80)


def drive_till_bump():
    u.move_servo(c.SERVO_JOINT,c.JOINT_MID)
    x.drive_speed(41, 100, True) #was 15
    #x.drive_speed(12, 100)
    #x.drive_condition(100, 100, u.found_bump, False)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)


def get_bin():
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED, 100)
    x.rotate(-86, 50)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    u.move_servo(c.SERVO_JOINT, c.JOINT_SWING)
    msleep(500)
    x.drive_speed(12, 70)
    u.move_servo(c.SERVO_JOINT, c.JOINT_SWING)
    u.move_bin(c.ARM_SWING, 5)
    u.move_servo(c.SERVO_JOINT, c.JOINT_PARALLEL, 5)
    # u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH, 5)
    u.move_bin(c.ARM_APPROACH, 5)
    u.move_servo(c.SERVO_JOINT, c.JOINT_ROTATE, 5)
    x.drive_speed(-20, 100)

def go_to_spinner():
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED, 5)
    x.drive_speed(10, 50)
    x.pivot_left(-90, 50)
    x.drive_speed(22, -100, True)
    x.pivot_left(-32, 50)
    x.drive_speed(-11, 60)
    x.pivot_right(-32, 50)
    x.drive_speed(-3, 50)
    x.drive_condition(50, 50, u.on_black_front, False)
    x.rotate(90, 30)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    u.move_servo(c.SERVO_JOINT, c.JOINT_PARALLEL)
    x.drive_condition(40, 40, u.on_black_front, False)
    x.drive_condition(40, 40, u.on_black_front, True)


    # x.drive_condition(25, 25, u.on_black_right)
    # x.pivot_right(15, 50)
    # x.drive_speed(6, 50)
    # x.pivot_left(-45, 50)
    # x.pivot_left_condition(-50, u.on_black_right, False)
    # u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    # u.move_servo(c.SERVO_JOINT, c.JOINT_APPROACH)
    # line_follow_untill_end_right()

    x.rotate_spinner(.25, 80)
    x.drive_speed(5,50)
    u.move_servo(c.SERVO_JOINT, c.JOINT_GROUND)
    x.rotate_spinner(4, -50)
    x.rotate_to_safe(50)


def go_to_ramp():
    display("Start of goToRamp")
    u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_ON)
    # x._drive(-53,-90)
    # msleep(3000)
    # u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    # x.drive_speed(-5,100)
    # x.pivot_right(-20, 50)
    # x.drive_speed(-8, 100)
    u.move_servo(c.SERVO_JOINT, c.JOINT_ARM_TILT)
    x.rotate(-7, 50)
    x.drive_forever(-50, -50)
    u.move_bin(c.ARM_TILT, 5)
    x.drive_speed(-10, 100)
    u.move_servo(c.SERVO_JOINT, c.JOINT_HOLD, 5)
    u.move_bin(c.ARM_TUCKED, 5)
    msleep(100)


    x.drive_speed(-5, 100)
    x.drive_speed(-5, 70)
    x.drive_speed(2, 50)
    x.pivot_right(-90, 60)
    u.move_servo(c.SERVO_JOINT, c.JOINT_MID)

    # u.wait_for_button()


def alt_init():
    u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_ON, 2047)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED, 2047)
    enable_servos()
    u.wait_for_button()
    x.drive_speed(70, 100)
    u.wait_for_button()

def go_up_ramp():
    display("Start of goUpRamp")
    # u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_APPROACH)
    # u.move_servo(c.SERVO_BIN_ARM, c.ARM_RAMP_APPROACH)
    # msleep(500)
    u.move_bin(c.ARM_SWING)
    # u.move_bin(c.ARM_RAMP_ON)
    x.drive_speed(12, 100)
    # msleep(500)
    # x.drive_speed(8, 100)
    # u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_APPROACH)
    # u.move_servo(c.SERVO_BIN_ARM, c.ARM_RAMP_ON)
    # msleep(500)
    #Line follows using right tophat until gyro y detects that were on the top of the hill
    #Disables servos after 5 seconds so that the servo arm doesnt
    #oscillate the robot causing the gyro to trigger early
    #TODO:
    #Fix line follow. Tophat might be too high when the robot raises up too high
    #Gyro value might need adjusting
    # x.drive_speed(8, 100)
    startTime = seconds()

    x.drive_speed(5, 100)
    while gyro_y() < 100 or seconds() < startTime + 2:
        if u.on_black_front():
            x.drive_forever(70, 100)
        else:
            x.drive_forever(100, 70)
        msleep(10)

    # count = 0
    # avg = accel_z()
    # while count < 5:
    #     if avg > -850:
    #         count = 0
    #     else:
    #         count += 1
    #     total = accel_z()
    #     for _ in range(0, 5):
    #         total += accel_z()
    #         if u.on_black_front():
    #             x.drive_forever(70, 100)
    #         else:
    #             x.drive_forever(100, 70)
    #         msleep(10)
    #     avg = total / 6


    # set_servo_position(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    # enable_servos()
    x.drive_speed(4, 100)
    # x.linefollow_distance(10)
    #     u.move_bin(c.ARM_ALL_UP)
    x.pivot_left_condition(30, u.on_black_front, False)
    x.pivot_right_condition(30, u.on_black_back, False)
    x.pivot_left_condition(30, u.on_black_front, False)
    # u.wait_for_button()
    u.move_bin(c.ARM_ALL_UP)
    msleep(500)
    u.move_servo(c. SERVO_JOINT, c.JOINT_DELIVER,4)
    msleep(500)
    x.linefollow_distance(27, 50, 70)
    x.pivot_right(-32.5, 50)
    disable_servo(c.SERVO_JOINT)
    msleep(500)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_MAX)
    msleep(500)
    x.drive_speed(1, 50)
    x.pivot_right(30, 50)
