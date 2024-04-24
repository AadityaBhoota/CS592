import math

def sumofFactors(n):
    sum = 0
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
            if (n // i) % 2 == 0 and (n // i) != i:
                sum += n // i
        i += 1

    return sum

# Test cases
assert sumofFactors(18) == 26
assert sumofFactors(30) == 48
assert sumofFactors(6) == 8

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)