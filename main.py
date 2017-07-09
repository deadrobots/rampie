#!/usr/bin/python

import actions as act
from utils import shutdown
from logger import log as display


def main():

    # act.test_ramp()
    # shutdown()

    display("Checking123")
    act.init()
    act.self_test()
    act.start()
    act.leave_startbox()
    act.drive_till_bump()
    act.get_bin()
    act.go_to_spinner()
    act.go_to_ramp()
    act.go_up_ramp()
    act.go_and_score_the_bin()
    shutdown()

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()