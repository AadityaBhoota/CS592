import math

def is_polite(n):
    # Helper function to calculate the nth polite number
    def polite_num(x):
        return 2 ** (x - 1) + x

    # Initialize variables
    x = 1
    count = 0

    # Find the nth polite number
    while True:
        if count == n:
            return polite_num(x)
        if math.gcd(x, 2 ** x) == 1:
            count += 1
        x += 1

# Test the function




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)