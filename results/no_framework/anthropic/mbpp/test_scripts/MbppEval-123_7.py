def amicable_numbers_sum(limit):
    """
    Calculates the sum of all amicable numbers up to the given limit.

    Args:
        limit (int): The upper bound for the range of numbers to check.

    Returns:
        int: The sum of all amicable numbers up to the given limit.
    """
    amicable_sum = 0
    for num in range(1, limit):
        if num != sum_of_divisors(sum_of_divisors(num)) and num == sum_of_divisors(num):
            amicable_sum += num
    return amicable_sum

def sum_of_divisors(n):
    """
    Calculates the sum of all proper divisors of a given number.

    Args:
        n (int): The number to find the sum of proper divisors for.

    Returns:
        int: The sum of all proper divisors of the given number.
    """
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)