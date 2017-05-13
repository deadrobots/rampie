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

# servos

servoBinClaw = 0
servoBinArm = 2


# servo values

binArmStraight = 850 #1240
binArmDown = 776
binArmDeliver = 2047
binArmCaster = 755

binClawDeliver = 1100
binClawRamp = 530
binClawCaster = 0

isClone = w.digital(CLONE_SWITCH)
