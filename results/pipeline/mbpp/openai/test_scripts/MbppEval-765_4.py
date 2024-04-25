import math

def is_polite(n):
    # Step 0: Check the input
    if not isinstance(n, int) or n <= 0:
        return None
    
    # Step 1: Calculate the sum of first n natural numbers
    sum_natural_numbers = n * (n + 1) // 2
    
    # Step 2: Calculate the square root of the sum obtained in step 1
    sqrt_sum = math.sqrt(sum_natural_numbers)
    
    # Step 3: Return the smallest integer greater than or equal to the square root as the nth polite number
    return math.ceil(sqrt_sum)

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)