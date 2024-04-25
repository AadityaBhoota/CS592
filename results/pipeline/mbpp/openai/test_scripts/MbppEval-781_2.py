import math 

def count_divisors(n):
    count = 0
    
    # Loop through numbers from 1 to sqrt(n)
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2 if n/i != i else 1
    
    # Check if count of divisors is even or odd
    if count % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)