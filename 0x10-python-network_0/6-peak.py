#!/usr/bin/python3
"""
python
"""

def find_peak(list_of_integers):

    if (list_of_integers):
        list_of_integers.sort()
        peak_ = list_of_integers[-1]

        return peak_

    else:
        return None
