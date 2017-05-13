from wallaby import *
import utils as u
import motorsPlusPlus as x
import constants as c


def upRamp():
    set_servo_position(c.servoBinArm, c.servoBinArmCaster)
    set_servo_position(c.servoBinClaw, c.servoBinClawCaster)
    enable_servos()
    u.waitForButton()
    x.drive_speed(22, 100)

    u.move_servo(c.servoBinArm, c.servoBinArmCaster)
    u.move_servo(c.servoBinClaw, c.servoBinClawRamp)
    u.move_servo(c.servoBinArm, c.servoBinArmStraight)

    msleep(3000)
    x.drive_speed(2, 75)
    while gyro_x() < 250 and gyro_y() < 250:
        if analog(0) > 1000:
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
    set_servo_position(c.servoBinArm, c.servoBinArmDeliver)
    x.linefollow_distance(23.46)

    u.DEBUGwithWait()

