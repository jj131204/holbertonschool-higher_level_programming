#!/usr/bin/python3


def write_file(filename="", text=""):

    with open(filename, 'w') as file_:

        file_.write(text)
        return len(text)
    file_.close()
