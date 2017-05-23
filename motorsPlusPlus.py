'''
Created on Aug 7, 2016
@author: graysonelias
'''

'''
This module tries to provide more accurate motor commands.
It requires boolean "isClone", integer "LMOTOR", and integer "RMOTOR" from a "constants" module.
These values refer to prime/clone status, the left motor's port, and the right motor's port respectively.
'''

from constants import IS_CLONE
from constants import LMOTOR
from constants import RMOTOR
# from constants import LTOPHAT

from utils import wait_for_button

from math import pi

from wallaby import ao
from wallaby import clear_motor_position_counter
from wallaby import freeze
from wallaby import get_motor_position_counter
# from wallaby import motor
from wallaby import msleep
from wallaby import seconds
from wallaby import analog
from wallaby import accel_x
from wallaby import motor_power as motor
from wallaby import motor_power

# Drive Constants
INCHES_TO_TICKS = 199
WHEEL_DISTANCE = 7.4 #205 - 4.25  # Distance between the two wheels
ADJUST = 1.01 #0.96

from wallaby import digital

if IS_CLONE:
    # Drive Constants
    INCHES_TO_TICKS = 165  # 169   #205 - 161     #156#127#50 cm #265
    WHEEL_DISTANCE = 4.25  # 205 - 4.25  # Distance between the two wheels
    ADJUST = 1  # adjust left wheel counter to fix drift


# Motor Control #

def _drive(left, right):  # Moves the robot using motor commands.
    motor(LMOTOR, left)
    motor(RMOTOR, right)



def _stop():  # Turns off all the motors.
    ao()


def drive_power(left, right):
    motor_power(LMOTOR, left)
    motor_power(RMOTOR, right)

def freeze_motors():  # Locks the motors to reduce drift.
    freeze(LMOTOR)
    freeze(RMOTOR)


def _right_ticks():  # Returns the right motor's tick count.
    return abs(get_motor_position_counter(RMOTOR))


def _left_ticks():  # Returns the left motor's tick count.
    return abs(get_motor_position_counter(LMOTOR) * ADJUST)


def _clear_ticks():  # Clears the motor ticks.
    clear_motor_position_counter(RMOTOR)
    clear_motor_position_counter(LMOTOR)





def arc_radius(angle, turnRadius, speed):  # Turns the robot "angle" degrees by arcing about "turnRadius".
    smallCircRadius = turnRadius - (WHEEL_DISTANCE / 2)
    largeCircRadius = turnRadius + (WHEEL_DISTANCE / 2)
    smallCircum = pi * 2 * smallCircRadius
    largeCircum = pi * 2 * largeCircRadius
    smallCircSeg = (angle / 360.0) * smallCircum
    largeCircSeg = (angle / 360.0) * largeCircum
    if turnRadius < 0:
        speed = -speed
    _clear_ticks()
    smallTicks = abs(INCHES_TO_TICKS * smallCircSeg)
    largeTicks = abs(INCHES_TO_TICKS * largeCircSeg)
    if angle > 0:
        smallSpeed = int(speed * (smallTicks / largeTicks))
        largeSpeed = int(speed)
        print smallTicks
        print largeTicks
        print smallTicks / largeTicks
        print smallSpeed
        print largeSpeed
        while _right_ticks() <= largeTicks:
            if (_right_ticks() / largeTicks) == (_left_ticks() / smallTicks):
                _drive(smallSpeed, largeSpeed)
            if (_right_ticks() / largeTicks) > (_left_ticks() / smallTicks):
                _drive(smallSpeed, int(largeSpeed / 1.3))
            if (_left_ticks() / smallTicks) > (_right_ticks() / largeTicks):
                _drive(int(smallSpeed / 1.3), largeSpeed)
    else:
        smallSpeed = int(speed * (smallTicks / largeTicks))
        largeSpeed = int(speed)
        print smallTicks
        print largeTicks
        print smallTicks / largeTicks
        print smallSpeed
        print largeSpeed
        while _left_ticks() <= largeTicks:
            if (_left_ticks() / largeTicks) == (_right_ticks() / smallTicks):
                _drive(largeSpeed, smallSpeed)
            if (_left_ticks() / largeTicks) > (_right_ticks() / smallTicks):
                _drive(largeSpeed, int(smallSpeed / 1.3))
            if (_right_ticks() / smallTicks) > (_left_ticks() / largeTicks):
                _drive(int(largeSpeed / 1.3), smallSpeed)
    freeze_motors()
    print smallTicks
    print largeTicks
    print get_motor_position_counter(RMOTOR)


from logger import data_log
from wallaby import magneto_x, magneto_y, magneto_z, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z

def drive_speed(inches, speed, accel=False):  # Drives an exact distance in inches.
    print "driving exact distance"

    scale = 1.3
    sum = 0

    max_error = 0
    max_sum = 0

    total_time = 0
    number_times = 0
    last_time = seconds()

    right = False

    if inches < 0:
        speed = -speed
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * inches)

    remain = 0
    if accel:
        for sp in range(1, speed, int(speed/10)):
            drive_timed_straight(sp, .025)
        remain = int((_left_ticks() + _right_ticks()) / 2)
        _clear_ticks()

    data_log("time\tmag_x\tmag_y\tmag_z\t\tgyr_x\tgyr_y\tgyr_z\tacc_x\tacc_y\tacc_z", "data.log")
    import constants as c
    c.startTime = seconds()
    while _right_ticks() <= ticks - remain:

        info = ("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d") % (seconds(), magneto_x(), magneto_y(), magneto_z(), gyro_x(), gyro_y(), gyro_z(), accel_x(), accel_y(), accel_z())
        data_log(info, "data.log")
        # print "info " + info

        left = _left_ticks()
        right = _right_ticks()
        error = right - left
        sum += error
        # if sum > 300:
        #     sum = 300
        # elif sum < -300:
        #     sum = -300
        if abs(sum) > abs(max_sum):
            max_sum = sum
        if abs(error) > max_error:
            max_error = abs(error)
            # print "hey!"
            # if right > left:
            #     motor_to_move = LMOTOR
            #     motor_to_not_move = RMOTOR
            # else:
            #     motor_to_move = RMOTOR
            #     motor_to_not_move = LMOTOR
            # ticks_to_get = get_motor_position_counter(motor_to_move) + error
            # if speed > 0:
            #     while get_motor_position_counter(motor_to_move) < ticks_to_get:
            #         motor(motor_to_move, speed)
            #         motor(motor_to_not_move, 0)
            # else:
            #     while get_motor_position_counter(motor_to_move) > ticks_to_get:
            #         motor(motor_to_move, speed)
            #         motor(motor_to_not_move, 00)

        p_scale = error * 0.018 # .015  osc at p = .04, T = 0.028 # P, p = .02 # PI, p = .018 i = 0.7714
        i_scale = sum * 0.001 #0.7714

        adjustment = p_scale + i_scale
        scale = abs(adjustment) + 1

        if adjustment == 0:
            _drive(speed, speed)
        elif adjustment > 0:
            right = True
            _drive(speed, int(speed / scale))
        elif adjustment < 0:
            if right:
                now = seconds()
                total_time += now - last_time
                last_time = now
                number_times += 1
                # print total_time / number_times
            right = False
            _drive(int(speed / scale), speed)

        # if right == left:
        #     _drive(speed, speed)
        # elif right > left:
        #     _drive(speed, int(speed / scale))
        # elif left > right:
        #     _drive(int(speed / scale), speed)

        # print "error %s, sum %s" % (error, sum)

    freeze_motors()
    print "max error: " + str(max_error)
    print "max sum: " + str(max_sum)
    print "current error " + str(error)
    print "current sum " + str(sum)

def drive_timed_straight(speed, time, clear=False):
    print "corrected driving for time"

    scale = 1.3
    sum = 0

    max_error = 0
    max_sum = 0

    total_time = 0
    number_times = 0
    last_time = seconds()
    if clear:
        _clear_ticks()

    start_time = seconds()

    while seconds() <= time + start_time:

        left = _left_ticks()
        right = _right_ticks()
        error = right - left
        sum += error
        # if sum > 300:
        #     sum = 300
        # elif sum < -300:
        #     sum = -300
        if abs(sum) > abs(max_sum):
            max_sum = sum
        if abs(error) > max_error:
            max_error = abs(error)
            # print "hey!"
            # if right > left:
            #     motor_to_move = LMOTOR
            #     motor_to_not_move = RMOTOR
            # else:
            #     motor_to_move = RMOTOR
            #     motor_to_not_move = LMOTOR
            # ticks_to_get = get_motor_position_counter(motor_to_move) + error
            # if speed > 0:
            #     while get_motor_position_counter(motor_to_move) < ticks_to_get:
            #         motor(motor_to_move, speed)
            #         motor(motor_to_not_move, 0)
            # else:
            #     while get_motor_position_counter(motor_to_move) > ticks_to_get:
            #         motor(motor_to_move, speed)
            #         motor(motor_to_not_move, 00)

        p_scale = error * 0.018  # .015  osc at p = .04, T = 0.028 # P, p = .02 # PI, p = .018 i = 0.7714
        i_scale = sum * 0.001  # 0.7714

        adjustment = p_scale + i_scale
        scale = abs(adjustment) + 1

        if adjustment == 0:
            _drive(speed, speed)
        elif adjustment > 0:
            right = True
            _drive(speed, int(speed / scale))
        elif adjustment < 0:
            if right:
                now = seconds()
                total_time += now - last_time
                last_time = now
                number_times += 1
                print total_time / number_times
            right = False
            _drive(int(speed / scale), speed)

        # if right == left:
        #     _drive(speed, speed)
        # elif right > left:
        #     _drive(speed, int(speed / scale))
        # elif left > right:
        #     _drive(int(speed / scale), speed)

        print "error %s, sum %s" % (error, sum)


def drive_timed(lmotor, rmotor, time):
    print "driving timed"
    _clear_ticks()
    end = seconds() + time
    if lmotor == 0 or rmotor == 0:
        print "please use pivot instead!"

    elif abs(rmotor) <= abs(lmotor):
        mod = rmotor / (lmotor * 1.0)
        newLeftSpeed = lmotor
        newRightSpeed = int(mod * lmotor)
    elif abs(lmotor) < abs(rmotor):
        mod = (lmotor * 1.0) / rmotor
        newLeftSpeed = int(mod * rmotor)
        newRightSpeed = rmotor
    while seconds() <= end:
        if int(_right_ticks() / mod) == int(_left_ticks() / mod):
            _drive(newLeftSpeed, newRightSpeed)
        if int(_right_ticks() / mod) > int(_left_ticks() / mod):
            _drive(newLeftSpeed, int(newRightSpeed / 1.3))
        if int(_left_ticks() / mod) > int(_right_ticks() / mod):
            _drive(int(newLeftSpeed / 1.3), newRightSpeed)
    freeze_motors()
print get_motor_position_counter(RMOTOR)


def drive_condition(lmotor, rmotor, testFunction,
                    state=True):  # Drives while "testFunction" returns "state" | an example would be: x.drive_condition(50, 50, x.getWait)
    print "driving under condition"
    _clear_ticks()
    if lmotor == 0 or rmotor == 0:
        print "this won't work! please use pivot_right_condition or pivot_left_condition instead!"
        exit(0)

    elif abs(rmotor) <= abs(lmotor):
        mod = rmotor / (lmotor * 1.0)
        newLeftSpeed = lmotor
        newRightSpeed = int(mod * lmotor)
    elif abs(lmotor) < abs(rmotor):
        mod = (lmotor * 1.0) / rmotor
        newLeftSpeed = int(mod * rmotor)
        newRightSpeed = rmotor
    while testFunction() is state:
        if int(_right_ticks() / mod) == int(_left_ticks() / mod):
            _drive(newLeftSpeed, newRightSpeed)
        if int(_right_ticks() / mod) > int(_left_ticks() / mod):
            _drive(newLeftSpeed, int(newRightSpeed / 1.3))
        if int(_left_ticks() / mod) > int(_right_ticks() / mod):
            _drive(int(newLeftSpeed / 1.3), newRightSpeed)
    freeze_motors()
    print get_motor_position_counter(RMOTOR)

def rotate(deg, speed):  # Rotates by using both wheels equally.
    if deg < 0:
        speed = -speed
        deg = -deg
    angle = deg / 360.0
    circ = pi * WHEEL_DISTANCE
    inches = angle * circ
    print circ
    print inches
    ticks = int(INCHES_TO_TICKS * inches)
    _clear_ticks()
    _drive(-speed, speed)
    while _right_ticks() <= ticks:
        pass
    freeze_motors()
    print get_motor_position_counter(RMOTOR)

def rotate_compass(deg, speed):  # Rotates by using both wheels equally.
    if deg < 0:
        speed = -speed
        deg = -deg
    angle = deg / 360.0
    circ = pi * WHEEL_DISTANCE
    inches = angle * circ
    print circ
    print inches
    ticks = int(INCHES_TO_TICKS * inches)
    _clear_ticks()
    _drive(-speed, speed)
    # data_log("time\tmag_x\tmag_y\tmag_z\t\tgyr_x\tgyr_y\tgyr_z\tacc_x\tacc_y\tacc_z", "data.log")
    # import constants as c
    # c.startTime = seconds()

    for _ in range(0, 10):
        magneto_x()
        magneto_y()
        msleep(10)

    mx = magneto_x()
    my = magneto_y()

    while abs(mx) > 100 or abs(my) > 100:
        mx = magneto_x()
        my = magneto_y()

    data = {"min_x": mx, "min_y": my, "max_x": mx, "max_y": my}

    while _right_ticks() <= ticks:
        # info = ("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d") % (
        # seconds(), magneto_x(), magneto_y(), magneto_z(), gyro_x(), gyro_y(), gyro_z(), accel_x(), accel_y(), accel_z())
        # data_log(info, "data.log")
        mag_x = magneto_x()
        mag_y = magneto_y()

        print(str(mag_x) + "\t" + str(mag_y))

        if mag_x > data["max_x"] and abs(mag_x - data["max_x"]) < 5: #  and abs(mag_x - data["max_x"])< 10
            data["max_x"] = mag_x
            # print("new max")
        if mag_y > data["max_y"] and abs(mag_y - data["max_y"]) < 5:
            data["max_y"] = mag_y
            print("new max y " + str(mag_y))
        if mag_x < data["min_x"] and abs(mag_x - data["min_x"]) < 5:
            data["min_x"] = mag_x
        if mag_y < data["min_y"] and abs(mag_y - data["min_y"]) < 5:
            data["min_y"] = mag_y

    freeze_motors()
    print get_motor_position_counter(RMOTOR)
    return data


def pivot_right(deg, speed):  # Pivots by moving the right wheel.
    if deg < 0:
        speed = -speed
        deg = -deg
    angle = deg / 360.0
    circ = pi * WHEEL_DISTANCE * 2
    inches = angle * circ
    ticks = int(INCHES_TO_TICKS * inches)
    _clear_ticks()
    _drive(0, speed)
    while _right_ticks() <= ticks:
        pass
    freeze_motors()

def pivot_right_condition(speed, testFunction, state=True):  # Pivots by moving the right wheel.
    _drive(0, speed)
    while testFunction() is state:
        pass
    freeze_motors()

def pivot_left(deg, speed):  # Pivots by moving the left wheel.
    if deg < 0:
        speed = -speed
        deg = -deg
    angle = deg / 360.0
    circ = pi * WHEEL_DISTANCE * 2
    inches = angle * circ
    ticks = int(INCHES_TO_TICKS * inches)
    _clear_ticks()
    _drive(speed, 0)
    while _left_ticks() <= ticks:
        pass
    freeze_motors()

def pivot_left_condition(speed, testFunction, state=True):  # Pivots by moving the left wheel.
    _drive(speed, 0)
    while testFunction() is state:
        pass
    freeze_motors()

def line_follow(distance):
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * distance)
    while _right_ticks() <= ticks:
        if analog(0) >1500:
            _drive(-40, -30)
        else:
            _drive(-30, -40)
    _drive(0,0)


def line_follow_forward(distance):
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * distance)
    while _right_ticks() <= ticks:
        if analog(0) >1500:
            _drive(30, 40)
        else:
            _drive(40, 30)
    _drive(0,0)

def line_follow_forward_end(port):
    i = 0
    while (i < 21):
        print i
        if analog(port) > 1500:
            i = 0
            drive_timed(30, 80, .02)
        else:
            i = i + 1
            drive_timed(80, 30, .02)

def change_adjust(x):
    global ADJUST
    if x:
        print("Adjusted to new value")
        ADJUST = .9685
    else:
        print("Resetting to old value")
        if IS_CLONE:
            ADJUST = 0.98
        else:
            ADJUST = 1.08
        ADJUST = 1.08 # add if clone 0.98


# def drive_speed_saw_black(inches, speed):  # Drives an exact distance in inches.
#     print "driving exact distance"
#     sawBlack = False
#     if inches < 0:
#         speed = -speed
#     _clear_ticks()
#     ticks = abs(INCHES_TO_TICKS * inches)
#     while _right_ticks() <= ticks:
#         if _right_ticks() == _left_ticks():
#             _drive(speed, speed)
#         if _right_ticks() > _left_ticks():
#             _drive(speed, int(speed / 1.3))
#         if _left_ticks() > _right_ticks():
#             _drive(int(speed / 1.3), speed)
#         if seeBlackRight() or seeBlackLeft():
#             sawBlack = True
#     freeze_motors()
#     print ticks
#     print get_motor_position_counter(RMOTOR)
#     if seeBlackRight() or seeBlackLeft():
#         return 0
#     elif sawBlack:
#         return 1
#     else:
#         return 2

#### AWFUL ATTTEMPTS TO CALIBRATE ####


def calibrate1(dist=0, num=0):  # WIP: Used to calibrate the constants for this module. Run as "calibrate()" to begin.
    if dist is 0:
        _clear_ticks()
        _drive(30, 30)
        msleep(3000)
        freeze_motors()
        print "Run the calibrate method again, but pass the distance traveled (inch) and the following number in:"
        print (_right_ticks() + _left_ticks()) / 2
    elif num is 0:
        drive_speed(6, 30)
        print "did it go " + str(dist) + " inches? If not, make slight adjustments to INCHES_TO_TICKS until it does."
    else:
        print "enter " + str(int(num / dist)) + " as INCHES_TO_TICKS. run calibrate again, but as calibrate(" + str(
            dist) + ", 0)"
    exit(0)

def calibrate2(inches=24, speed=50):
    global lAdjust
    global INCHES_TO_TICKS
    INCHES_TO_TICKS = 0
    lAdjust = 1

    if inches < 0:
        speed = -speed
    _clear_ticks()
    ticks = abs(INCHES_TO_TICKS * inches)

    prevAdjust = -1

    while True:
        start = seconds()
        lStart = start
        rStart = start
        lTime = -1
        rTime = -1
        l = False
        r = False
        i = 0
        _clear_ticks()

        while not l or not r:
            if l and not r:
                i = i + 1
            elif r and not l:
                i = i - 1

            if analog(2) > 1500:
                if not l:
                    lTime = seconds() - lStart
                l = True
                print("LEFT")
            if analog(3) > 1500:
                if not r:
                    rTime = seconds() - rStart
                r = True
                print("RIGHT")

            if _right_ticks() == _left_ticks():
                _drive(speed, speed)
            if _right_ticks() > _left_ticks():
                _drive(speed, int(speed / 1.3))
            if _left_ticks() > _right_ticks():
                _drive(int(speed / 1.3), speed)

        # if i < 0:
        #     lAdjust = lAdjust + (0.0005 * i)
        # elif i > 0:
        #     lAdjust = lAdjust - (0.0005 * i)

        lAdjust = rTime / lTime

        if prevAdjust != -1:
            lAdjust = (lAdjust + prevAdjust) / 2

        INCHES_TO_TICKS = ((_left_ticks() + _right_ticks()) / 2) / inches

        drive_timed(-50, -50, int(seconds() - start))

        print("lTime: " + str(lTime) + "\trTime: " + str(rTime))
        print("ROT: " + str(i))
        print("ADJ: " + str(lAdjust))
        print("I2T: " + str(INCHES_TO_TICKS) + "\n")

        if i == 0:
            break

        wait_for_button()

def calibrate3():
    AMOUNT = 6000
    _clear_ticks()
    _drive(50, 50)
    startR = seconds()
    while _right_ticks() < AMOUNT:
        pass
    endR = seconds() - startR
    freeze_motors()
    msleep(5000)
    _clear_ticks()
    _drive(50, 50)
    startL = seconds()
    while _left_ticks() < AMOUNT:
        pass
    endL = seconds() - startL

    print "Value: " + str(endL / endR)



from wallaby import digital

def calibrate5():
    _clear_ticks()
    while not digital(13):
        try:
            print str(_left_ticks()) + " " + str(_right_ticks()) + " " + str(_right_ticks() / _left_ticks())
        except Exception:
            pass
        msleep(100)
    x = _right_ticks() / _left_ticks()
    global lAdjust
    lAdjust = x
    print(x)
    # open(("adjust-" + str(isClone)), "w").write(str(x))

def calibrate6():
    global lAdjust
    lAdjust = 1

    while True:
        drive_speed(3, 50)
        if analog(0) > 1500:
            lAdjust = lAdjust + 0.05
            while not digital(13):
                pass
                msleep(500)
        elif analog(0) < 1000:
            lAdjust = lAdjust - 0.05
            while not digital(13):
                pass
            msleep(500)
        print lAdjust

from wallaby import right_button, left_button

# def calibrate7():
#     global lAdjust
#     lAdjust = 1
#     while True:
#         drive_speed(10, 100)
#         while True:
#             if right_button():
#                 lAdjust = lAdjust + .05
#                 break
#             elif left_button()\
#
#                     :
#                 lAdjust = lAdjust - .05
#                 break
#     print lAdjust
#     msleep(500)

def linefollow_distance(distance):
    _clear_ticks()
    while _right_ticks() < distance * INCHES_TO_TICKS:
        if analog(0) <1500:
            _drive(100, 80)
        else:
            _drive(80, 100)


def drive_forever(left, right):
    _drive(left, right)
