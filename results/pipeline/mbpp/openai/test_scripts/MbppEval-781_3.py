import math 

def count_divisors(n):
    divisors = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)
                
    count = len(divisors)
    
    if count % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)