import math

def sumofFactors(n):
    # Initialize sum as 1 because 1 will always be a factor
    s = 1
    # Loop through numbers from 2 to square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        # If i is a factor of n
        if n % i == 0:
            # If i is even, add it to the sum
            if i % 2 == 0:
                s += i
            # If n/i is even and not equal to i, add it to the sum
            if (n//i) % 2 == 0 and (n//i) != i:
                s += n//i
    return s

# Test cases




def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)