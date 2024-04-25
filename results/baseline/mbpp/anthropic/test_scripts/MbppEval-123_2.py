def amicable_numbers_sum(limit):
    """
    Write a function to sum all amicable numbers from 1 to a specified number.

    Examples:
    amicable_numbers_sum(999) == 504
    amicable_numbers_sum(9999) == 31626
    amicable_numbers_sum(99) == 0
    """
    def divisors_sum(n):
        """Helper function to calculate the sum of proper divisors of a number"""
        return sum(i for i in range(1, n) if n % i == 0)

    amicable_numbers = set()
    total_sum = 0

    for i in range(1, limit):
        a = divisors_sum(i)
        b = divisors_sum(a)
        if i == b and a != b:
            amicable_numbers.add(i)
            amicable_numbers.add(a)
            total_sum += i

    return total_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)