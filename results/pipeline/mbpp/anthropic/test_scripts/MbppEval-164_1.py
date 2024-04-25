import math

def div_sum(n):
    divisor_sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum

def areEquivalent(a, b):
    a_divisor_sum = div_sum(a)
    b_divisor_sum = div_sum(b)
    return a_divisor_sum == b_divisor_sum

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)