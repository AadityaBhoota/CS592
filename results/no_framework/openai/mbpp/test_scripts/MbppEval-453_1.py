import math 

def sumofFactors(n):
    total_sum = 0
    sqrt_n = int(math.sqrt(n))

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            if i % 2 == 0:
                total_sum += i
            if (n // i) % 2 == 0 and (n // i) != i:
                total_sum += n // i

    return total_sum

# Test Cases




def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)