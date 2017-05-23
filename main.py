#!/usr/bin/python

import actions as act


def main():
    print "Check"
    act.init()
    act.find_black_line()
    act.drive_till_bump()
    act.get_bin()
    act.go_to_ramp()
    exit(0)

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()