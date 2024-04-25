def amicable_numbers_sum(limit):
    amicable_numbers = []

    for n in range(1, limit + 1):
        divisor_sum = sum(divisor for divisor in range(1, n) if n % divisor == 0)
        if divisor_sum != n and sum(divisor for divisor in range(1, divisor_sum) if divisor_sum % divisor == 0) == n:
            amicable_numbers.append(n)

    return sum(amicable_numbers)

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)