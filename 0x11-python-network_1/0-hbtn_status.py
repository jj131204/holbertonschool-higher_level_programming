#!/usr/bin/python3
"""python"""


from urllib import request

if __name__ == "__main__":
    """ Python script that fetches https://intranet.hbtn.io/status """

    url = request.Request("https://intranet.hbtn.io/status")

    with request.urlopen(url) as new:
        test = new.read()

    print("Body response:")
    print("\t- type: {}".format(type(test)))
    print("\t- content: {}".format(test))
    print("\t- utf8 content: {}".format(test.decode("utf-8")))
