import math

def next_Perfect_Square(N):
    # Calculate the square root of the given number
    sqrt_n = math.isqrt(N)
    
    # Check if the square of the square root is the same as the original number
    if sqrt_n * sqrt_n == N:
        # If the given number is already a perfect square, return the next perfect square
        return (sqrt_n + 1) ** 2
    else:
        # If the given number is not a perfect square, return the square of the next integer
        return (sqrt_n + 1) ** 2

# Test cases




def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)