import math

def is_triangular(num):
    # Check if a number is a triangular number
    n = int(math.sqrt(2*num))
    return n*(n+1)//2 == num

def find_Index(n):
    # Find the index of the smallest triangular number with n digits
    digits = 1
    num = 1

    while True:
        if math.floor(math.log10(num)) + 1 == n and is_triangular(num):
            return num

        digits += 1
        num += digits

# Test the function with examples




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)