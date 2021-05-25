#!/usr/binpython3


def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

a = 10

for i in range(a):
    if i < 5:
        print("menor que 5")
    else:
        print("mayor que 5")
