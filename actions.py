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


def self_test():
    if u.on_black_left() or u.on_black_right():
        display("Something is wrong with the tophats!")
        display("LTOPHAT: {}\tRTOPHAT: {}".format(u.on_black_left(), u.on_black_right()))
    while not u.found_bump():
        pass
    display("Good gyro")
    u.wait_for_button()
    enable_servos()
    x.drive_forever(80, 80)
    while not u.on_black_left() or not u.on_black_right():
        pass
    x.freeze_motors()
    u.move_servo(c.SERVO_JOINT, c.JOINT_MID)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_SPINNER_TEST)
    x.wait_for_someone_to_rotate()
    u.wait_for_button()
    x.rotate_until_stalled(20)
    msleep(500)
    x.rotate_spinner(.056, -30)
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
    find_black_line()
    x.pivot_left(-90, 60)
    x.drive_speed(-4, 100)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    find_black_line()
    x.drive_speed(8, 80)
    x.pivot_right(-90, 60)
    x.drive_speed(-5, 100)


def find_black_line():
    display ("In one")
    x.drive_forever(60, 60)
    while not u.on_black_left() and not u.on_black_right():
        print "while"
    x.freeze_motors()


def drive_till_bump():
    u.move_servo(c.SERVO_JOINT,c.JOINT_APPROACH)
    x.drive_speed(15,100, True)
    u.move_servo(c.SERVO_JOINT,c.JOINT_MID)
    x.drive_speed(25, 100)
    x.drive_condition(100, 100, u.found_bump, False)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)


def get_bin():
    u.move_servo(c.SERVO_JOINT, c.JOINT_TUCKED, 100)
    x.drive_speed(3, 50)  # 4
    x.pivot_left(45, 50)
    x.rotate(-50, 50) #was -52
    x.drive_speed(-8, 100) #-8
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    u.move_servo(c.SERVO_JOINT, c.JOINT_APPROACH)
    msleep(500)
    x.drive_speed(13, 30)
    u.move_servo(c.SERVO_JOINT, c.JOINT_SWING)
    u.move_bin(c.ARM_SWING, 5)
    u.move_servo(c.SERVO_JOINT, c.JOINT_PARALLEL)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    u.move_servo(c.SERVO_JOINT, c.JOINT_HOLD)
    x.drive_speed(-30, 100)

def go_to_spinner():
    u.move_servo(c.SERVO_JOINT, c.JOINT_ROTATE)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    x.drive_speed(10, 50)
    x.pivot_left(-100, 50)
    x.drive_speed(22, -100, True)
    x.pivot_left(-42, 50)
    x.drive_speed(-18, 60)
    x.pivot_right(-35, 50)
    x.drive_speed(-6, 50)
    x.drive_condition(50, 50, u.on_black_right, False)
    x.drive_condition(25, 25, u.on_black_right)
    x.pivot_right(15, 50)
    x.drive_speed(6, 50)
    x.pivot_left(-45, 50)
    x.pivot_left_condition(-50, u.on_black_right, False)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    u.move_servo(c.SERVO_JOINT, c.JOINT_APPROACH)
    line_follow_untill_end_right()
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    u.move_servo(c.SERVO_JOINT, c.JOINT_PARALLEL)
    x.rotate_spinner(.25, -80)
    x.drive_speed(3,50)
    u.move_servo(c.SERVO_JOINT, c.JOINT_GROUND)
    x.rotate_spinner(4,75)
    x.rotate_to_safe()

def line_follow_untill_end_right():
    while not u.on_black_left():
        state = u.on_black_right()
        if state:
            x.drive_forever(50, 30)
        else:
            x.drive_forever(30, 50)
        msleep(10)
    while u.on_black_left():
        state = u.on_black_right()
        if state:
            x.drive_forever(50, 30)
        else:
            x.drive_forever(30, 50)
        msleep(10)
    x.freeze_motors()


def go_to_ramp():
    display("Start of goToRamp")
    u.move_servo(c.SERVO_JOINT, c.JOINT_ROTATE)
    x._drive(-53,-90)
    msleep(3000)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_APPROACH)
    x.drive_speed(-5,100)
    x.pivot_right(-20, 50)
    x.drive_speed(-8, 100)
    u.wait_for_button()


def go_up_ramp():
    display("Start of goUpRamp")
    u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_APPROACH)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_RAMP_APPROACH)
    msleep(500)
    x.drive_speed(8, 100)
    msleep(500)
    x.drive_speed(8, 100)
    u.move_servo(c.SERVO_JOINT, c.JOINT_RAMP_APPROACH)
    u.move_servo(c.SERVO_BIN_ARM, c.ARM_RAMP_ON)
    msleep(500)
    #Line follows using right tophat until gyro y detects that were on the top of the hill
    #Disables servos after 5 seconds so that the servo arm doesnt
    #oscillate the robot causing the gyro to trigger early
    #TODO:
    #Fix line follow. Tophat might be too high when the robot raises up too high
    #Gyro value might need adjusting
    x.drive_speed(8, 100)
    startTime = seconds()

    count = 0

    while count < 15:
        display((accel_z()))
        if seconds()-startTime > 5:
            disable_servos()

        if accel_z() > -800:
            count = 0
        else:
            count += 1
        if u.on_black_right():
            x.drive_forever(100, 80)
        else:
            x.drive_forever(80, 100)
        msleep(10)
    set_servo_position(c.SERVO_BIN_ARM, c.ARM_TUCKED)
    enable_servos()
