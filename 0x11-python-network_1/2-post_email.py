#!/usr/bin/python3
"""python"""


from urllib import request
from sys import argv


if __name__ == "__main__":
    """ ...  """

    data = {'email': argv[2]}
    arg1 = argv[1]
    url = request.Request(arg1, data)

    with request.urlopen(url) as new:
        print(new.read().decode("utf-8"))
