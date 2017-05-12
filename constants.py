


import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 0
RMOTOR = 3

# Digital ports
LEFT_BUTTON = 0
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

#servos
servoBinArm = 2
servoBinArmStraight = 1240
servoBinArmDown = 776
servoBinArmDeliver = 2047
servoBinArmCaster = 755

servoBinClaw = 0
servoBinClawCaster = 0
isClone = w.digital(CLONE_SWITCH)
