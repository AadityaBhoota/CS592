def amicable_numbers_sum(limit):
    """
    Write a function to sum all amicable numbers from 1 to a specified number.

    Examples:
    amicable_numbers_sum(999) == 504
    amicable_numbers_sum(9999) == 31626
    amicable_numbers_sum(99) == 0
    """
    amicable_numbers = set()

    for num in range(1, limit):
        divisors_sum = sum(div for div in range(1, num) if num % div == 0)
        other_num_divisors_sum = sum(div for div in range(1, divisors_sum) if divisors_sum % div == 0)

        if other_num_divisors_sum == num and num != divisors_sum:
            amicable_numbers.add(num)
            amicable_numbers.add(divisors_sum)

    return sum(amicable_numbers)

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)