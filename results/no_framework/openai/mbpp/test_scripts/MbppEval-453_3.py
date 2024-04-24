import math 

def sumofFactors(n):
    total_sum = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                total_sum += i
            if i != n // i and (n // i) % 2 == 0:
                total_sum += n // i
    return total_sum

# Test cases




def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)