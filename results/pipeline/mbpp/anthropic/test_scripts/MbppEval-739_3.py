import math

def find_Index(n):
    number = 1
    index = 0
    while len(str(number)) < n:
        index += 1
        number += index
    return int((math.sqrt(8 * number + 1) - 1) / 2)

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)