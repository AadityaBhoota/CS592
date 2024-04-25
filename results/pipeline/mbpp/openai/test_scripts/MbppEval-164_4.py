import math 

def div_sum(n): 
    sum_divisors = sum(get_divisors(n))
    return sum_divisors

def get_divisors(n):
    divisors = [1]  # Include 1 as a divisor
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid duplicate square root divisor
                divisors.append(n // i)
    return divisors

def are_equivalent(m, n):
    return div_sum(m) == div_sum(n)

# Test cases
assert are_equivalent(36, 57) == False
assert are_equivalent(2, 4) == False
assert are_equivalent(23, 47) == True

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)