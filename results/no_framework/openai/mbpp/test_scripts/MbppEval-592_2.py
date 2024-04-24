def binomial_coeff(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coeff(n-1, k-1) + binomial_coeff(n-1, k)

def sum_of_product(num):
    total_sum = 0
    for i in range(1, num + 1):
        total_sum += binomial_coeff(num, i) * binomial_coeff(num, i-1)
    return total_sum

# Examples




def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)