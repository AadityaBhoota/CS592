def amicable_numbers_sum(limit):
    """
    Write a function to sum all amicable numbers from 1 to a specified number.

    Examples:
    amicable_numbers_sum(999) == 504
    amicable_numbers_sum(9999) == 31626
    amicable_numbers_sum(99) == 0
    """
    total_sum = 0

    for num in range(1, limit):
        divisor_sum = sum(divisor for divisor in range(1, num) if num % divisor == 0)
        if divisor_sum != num and sum(divisor for divisor in range(1, divisor_sum) if divisor_sum % divisor == 0) == num:
            total_sum += num

    return total_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)