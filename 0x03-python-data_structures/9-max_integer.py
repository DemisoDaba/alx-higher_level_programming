#!/usr/bin/python3
def max_integer(my_list = []):
    if not my_list:
        return (None)
    largest = my_list[0]
    for count in range(1, len(my_list)):
        if my_list[count] > largest:
            largest = my_list[count]
    return (largest)
large = max_integer()
print(large)
