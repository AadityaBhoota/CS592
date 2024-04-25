import math

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If the number is a perfect square
            if n // i == i:
                count += 1
            # Otherwise count both divisors
            else:
                count += 2
                
    return "Even" if count % 2 == 0 else "Odd"

# Testing the function




def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)