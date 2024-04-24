def amicable_numbers_sum(limit):
    """
    Sum all amicable numbers from 1 to a specified number.

    An amicable number is a number for which the sum of the proper divisors of one
    (the numbers less than the number and which divide it) is equal to the other
    number.

    Args:
        limit (int): The upper limit to search for amicable numbers.

    Returns:
        int: The sum of all amicable numbers up to the specified limit.
    """
    total_sum = 0

    for i in range(1, limit):
        divisor_sum_i = sum(divisor for divisor in range(1, i) if i % divisor == 0)
        divisor_sum_j = sum(divisor for divisor in range(1, divisor_sum_i) if divisor_sum_i % divisor == 0)

        if i == divisor_sum_j and i != divisor_sum_i:
            total_sum += i

    return total_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)