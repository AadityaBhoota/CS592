import math

def divisor(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2  # Increment count for both 'i' and 'n // i'
    
    if sqrt_n * sqrt_n == n:
        count -= 1  # Decrement count if sqrt(n) is a divisor
    
    return count

def check(candidate):
    assert divisor(15) == 4
    assert divisor(12) == 6
    assert divisor(9) == 3

check(divisor)