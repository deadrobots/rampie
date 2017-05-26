import wallaby as w

# Time
startTime = w.seconds()

# Motor ports
LMOTOR = 0
RMOTOR = 3

# Digital ports
LEFT_BUTTON = 0
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

# servos

SERVO_BIN_CLAW = 0
SERVO_BIN_ARM = 2

# servo values
BIN_ARM_IN = 190
BIN_ARM_STRAIGHT = 850
BIN_ARM_DOWN = 776
BIN_ARM_DELIVER = 2047
BIN_ARM_DRIVE = 755

BIN_CLAW_DELIVER = 1100
BIN_CLAW_RAMP = 530
BIN_CLAW_CASTER = 0
BIN_UP_RAMP = 1225

IS_CLONE = w.digital(CLONE_SWITCH)

arm = 2
claw = 1
joint = 0

arm_down = 700
arm_up = 1263
arm_all_up = 2047
arm_tucked = 241
arm_half_tucked = 450

claw_open = 1380
claw_close = 377

joint_mid = 0 #1750
joint_tucked = 1947 #432
