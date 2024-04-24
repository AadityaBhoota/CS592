def amicable_numbers_sum(limit):
    def sum_of_divisors(n):
        divisors_sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors_sum += i
                if n // i != i:
                    divisors_sum += n // i
        return divisors_sum
    
    amicable_sum = 0
    for a in range(2, limit + 1):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_sum += a
    
    return amicable_sum


# Test cases




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)