def amicable_numbers_sum(limit):
    """
    Write a function to sum all amicable numbers from 1 to a specified number.

    Examples:
    amicable_numbers_sum(999) == 504
    amicable_numbers_sum(9999) == 31626
    amicable_numbers_sum(99) == 0
    """
    total_sum = 0

    for i in range(1, limit):
        if i != sum_of_divisors(sum_of_divisors(i)) and i == sum_of_divisors(i):
            total_sum += i

    return total_sum

def sum_of_divisors(n):
    """
    Helper function to calculate the sum of all proper divisors of a number.
    """
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

# Example usage




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)