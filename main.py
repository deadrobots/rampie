#!/usr/bin/python

import actions as act


def main():
    print "Checking"
    # act.init()
    # act.test()
    # exit(0)

    # act.test()

    act.start()
    act.leave_startbox()
    act.drive_till_bump()
    act.get_bin()
    act.go_to_spinner()
    # act.go_to_ramp()
    exit(0)

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()