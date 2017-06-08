#!/usr/bin/python

import actions as act
from utils import shutdown
from logger import log as display

def main():
    display("Checking")
    act.self_test()
    act.start()
    act.leave_startbox()
    act.drive_till_bump()
    act.get_bin()
    act.go_to_spinner()
    act.go_to_ramp()
    act.go_up_ramp()
    shutdown()

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()