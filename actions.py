from wallaby import *
import utils as u
import motorsPlusPlus as x
import constants as c


def upRamp():
    set_servo_position(c.servoBinArm, c.binArmStraight)
    # set_servo_position(c.servoBinClaw, c.binClawCaster)
    enable_servos()
    u.waitForButton()
    x.drive_speed(22, 100)

    # u.move_servo(c.servoBinArm, c.binArmCaster)
    # u.move_servo(c.servoBinClaw, c.binClawRamp)
    # u.move_servo(c.servoBinArm, c.binArmStraight)

    msleep(3000)
    x.drive_speed(2, 75)
    while gyro_y() > -350 and gyro_y() > -350:
        print(gyro_y())
        if analog(0) < 1000:
            x._drive(60, 100)
        else:
            x._drive(100, 80)
    print(gyro_x())
    print(gyro_y())

    # x.freeze_motors()
    #
    # u.waitForButton()

    x.drive_speed(6, 100)

    # this is where it stops at the top

    msleep(2500)
    #u.move_servo(c.servoBinClaw, c.servoBinClawDeliver)
    set_servo_position(c.servoBinArm, c.binArmDeliver)
    x.linefollow_distance(23.46)

    u.DEBUGwithWait()

