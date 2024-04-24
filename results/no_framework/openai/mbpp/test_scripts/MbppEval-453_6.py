def sumofFactors(n):
    result = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                result += i
            if i != n // i and (n // i) % 2 == 0:
                result += n // i
    return result

# Test cases




def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)