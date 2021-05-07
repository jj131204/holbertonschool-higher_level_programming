#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy = my_list.copy()
    add = 0
    for i in my_list:
        for j in (0, i):
            if my_list[i] == copy[j]:
                break
            else:
                add = add + i
    return add
