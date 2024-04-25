def sum(a, b):
    # Find common divisors of a and b
    divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
    
    # Calculate the sum of common divisors
    result = sum(divisors)
    
    return result

# Test cases




def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)