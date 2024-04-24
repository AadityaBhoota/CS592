def even_Power_Sum(n):
    """
    Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.

    Examples:
    even_Power_Sum(2) == 1056
    even_Power_Sum(3) == 8832
    even_Power_Sum(1) == 32
    """
    total_sum = 0
    for i in range(1, n+1):
        total_sum += (2*i)**5
    return total_sum

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)