def amicable_numbers_sum(limit):
    """
    Sum all amicable numbers from 1 to the specified limit.

    An amicable pair is a set of two different numbers where each of them is the sum of the proper divisors of the other.

    Args:
        limit (int): The upper limit to search for amicable numbers.

    Returns:
        int: The sum of all amicable numbers found within the specified limit.
    """
    amicable_sum = 0

    for num in range(1, limit):
        d1 = sum([div for div in range(1, num) if num % div == 0])
        d2 = sum([div for div in range(1, d1) if d1 % div == 0])

        if d2 == num and d1 != d2:
            amicable_sum += num

    return amicable_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)