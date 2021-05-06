#!/usr/bin/python3
def no_c(my_string):
    new_string = [j for j in my_string if j != 'c' and j != 'C']
    return ("".join(new_string))
