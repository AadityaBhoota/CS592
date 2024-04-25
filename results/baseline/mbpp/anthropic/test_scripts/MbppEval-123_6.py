def is_amicable(n):
    """
    Checks if a number is amicable.
    
    An amicable number is a pair of numbers where the sum of the proper divisors of one number is equal to the other number.
    """
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum != n and sum(i for i in range(1, divisors_sum) if divisors_sum % i == 0) == n

def amicable_numbers_sum(limit):
    """
    Sums all amicable numbers from 1 to the specified limit.
    """
    return sum(n for n in range(1, limit) if is_amicable(n))

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)