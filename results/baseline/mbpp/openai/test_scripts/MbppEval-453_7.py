import math

def sumofFactors(n):
    # Initialize sum to 0
    sum_factors = 0
    
    # Iterate from 1 to square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        # Check for factors
        if n % i == 0:
            # If factor is even, add it to sum
            if i % 2 == 0:
                sum_factors += i
            # Check if both factors are not same
            if n // i != i and (n // i) % 2 == 0:
                sum_factors += n // i
                
    return sum_factors

# Test the function




def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)