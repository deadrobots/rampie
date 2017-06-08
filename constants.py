import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
SPINNER = 2
RMOTOR = 0

# Digital ports
LEFT_BUTTON = 0
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

#Analog ports
BACK_TOPHAT = 0
FRONT_TOPHAT = 5

IS_CLONE = w.digital(CLONE_SWITCH)

# Thresholds
THRESHOLD_GYRO = 200
THRESHOLD_TOPHAT = 2000

# Servos
SERVO_BIN_ARM = 2
SERVO_JOINT = 0

OFFSET_ARM = 0
OFFSET_JOINT = 0
if IS_CLONE:
    OFFSET_ARM = 80
    OFFSET_JOINT = -48

# Servo values
ARM_RAMP_APPROACH = 480 + OFFSET_ARM
ARM_APPROACH = 500 + OFFSET_ARM
ARM_ALL_UP = 2047 + OFFSET_ARM
ARM_TUCKED = 241 + OFFSET_ARM
ARM_SPINNER_TEST = 570 + OFFSET_ARM
ARM_SWING = 800 + OFFSET_ARM
ARM_RAMP_ON = 1120 + OFFSET_ARM

JOINT_RAMP_APPROACH = 1205 + OFFSET_JOINT
JOINT_APPROACH = 1175 + OFFSET_JOINT
JOINT_TUCKED = 0 + OFFSET_JOINT
JOINT_HOLD = 625 + OFFSET_JOINT
JOINT_MID = 575 + OFFSET_JOINT
JOINT_ROTATE = 300 + OFFSET_JOINT
JOINT_PARALLEL = 775 + OFFSET_JOINT
JOINT_GROUND = 1025 + OFFSET_JOINT
JOINT_SWING = 950 + OFFSET_JOINT
JOINT_RAMP_ON = 400 + OFFSET_JOINT
JOINT_DELIVER = 1850

LOGFILE = "" # Leave empty
ROBOT_NAME = "RampyV2"
