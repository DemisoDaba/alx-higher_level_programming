#!/usr/bin/python3
def switch_values(a, b):
    a, b = b, a
    return a, b

a = 89
b = 10

print("Before switching:")
print("a={:d} - b={:d}".format(a, b))

a, b = switch_values(a, b)

print("After switching:")
print("a={:d} - b={:d}".format(a, b))
