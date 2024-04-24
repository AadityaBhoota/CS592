def amicable_numbers_sum(limit):
    def divisor_sum(n):
        return sum([i for i in range(1, n) if n % i == 0])

    def is_amicable_pair(a, b):
        return (divisor_sum(a) == b) and (divisor_sum(b) == a) and (a != b)

    amicable_sum = 0
    for i in range(1, limit):
        if is_amicable_pair(i, divisor_sum(i)):
            amicable_sum += i

    return amicable_sum


# Test cases




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)