def binomial_Coeff(n):
    """
    Write a python function to find the sum of the product of consecutive binomial coefficients.

    Examples:
    binomial_Coeff(3) == 15
    binomial_Coeff(4) == 56
    binomial_Coeff(1) == 1
    """
    if n == 0 or n == 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(i, -1, -1):
            if j == 0 or j == i:
                dp[j] = 1
            else:
                dp[j] = dp[j - 1] + dp[j]

    result = 0
    for i in range(1, n):
        result += dp[i] * dp[i + 1]

    return result

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)