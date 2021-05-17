#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        j = fct(*args)
        return j
    except Exception as test:
        print("Exception: {}".format(test), file=sys.stderr)
        return None
