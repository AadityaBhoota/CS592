import math

def find_Index(n):
    index = 1
    num_digits = 0
    i = 2

    while True:
        # Calculate the next triangular number
        triangular_num = i * (i + 1) // 2
        i += 1

        # Check the number of digits in the triangular number
        num_digits = int(math.log10(triangular_num)) + 1

        if num_digits == n:
            return index

        index += 1

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)