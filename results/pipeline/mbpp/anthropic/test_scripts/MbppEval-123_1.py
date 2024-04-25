def amicable_numbers_sum(limit):
    amicable_numbers = []

    for n in range(1, limit + 1):
        divisor_sum = sum(i for i in range(1, n) if n % i == 0)
        if sum(i for i in range(1, divisor_sum) if divisor_sum % i == 0) == n and n != divisor_sum:
            amicable_numbers.append(n)

    return sum(amicable_numbers)

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)