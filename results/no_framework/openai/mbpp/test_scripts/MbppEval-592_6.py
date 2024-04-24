from math import comb

def sum_Of_product(n):
    total = 0
    for k in range(n):
        total += comb(n, k) * comb(n, k + 1)
    return total

# Test cases




def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)