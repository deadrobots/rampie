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

    u.move_servo(2, 1400)

    msleep(3000)
    x.drive_speed(2, 75)
    while gyro_x() < 200 and gyro_y() < 200:
        if analog(0) > 1000:
            x._drive(60, 100)
        else:
            x._drive(100, 80)
    print(gyro_x())
    print(gyro_y())

    x.drive_speed(6, 100)

    # this is where it stops at the top

    exit(0)

    msleep(2500)
    set_servo_position(2, 1400)

    x.linefollow_distance(15)
    x.drive_speed(20, -100)
