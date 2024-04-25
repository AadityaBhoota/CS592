def amicable_numbers_sum(limit):
    def proper_divisors_sum(n):
        return sum([i for i in range(1, n) if n % i == 0])

    def is_amicable(a):
        b = proper_divisors_sum(a)
        return a != b and a == proper_divisors_sum(b)

    amicable_sum = sum([i for i in range(1, limit) if is_amicable(i)])

    return amicable_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)