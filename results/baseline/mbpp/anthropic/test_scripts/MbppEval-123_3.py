def amicable_numbers_sum(limit):
    """
    Write a function to sum all amicable numbers from 1 to a specified number.

    Examples:
    amicable_numbers_sum(999) == 504
    amicable_numbers_sum(9999) == 31626
    amicable_numbers_sum(99) == 0
    """
    total = 0
    for num in range(1, limit):
        d1 = sum_proper_divisors(num)
        d2 = sum_proper_divisors(d1)
        if num == d2 and num != d1:
            total += num
    return total

def sum_proper_divisors(n):
    """
    Helper function to calculate the sum of proper divisors of a number.
    """
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)