def sumofFactors(n):
    even_factors_sum = 0
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                even_factors_sum += i
            if i != n // i and (n // i) % 2 == 0:
                even_factors_sum += n // i
    
    return even_factors_sum

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)