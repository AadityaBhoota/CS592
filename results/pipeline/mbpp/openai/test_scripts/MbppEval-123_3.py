def amicable_numbers_sum(limit):
    def sum_proper_divisors(num):
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum

    total_sum = 0
    for i in range(1, limit + 1):
        divisors_sum_i = sum_proper_divisors(i)
        
        if divisors_sum_i != i and divisors_sum_i <= limit:
            if i == sum_proper_divisors(divisors_sum_i):
                total_sum += i

    return total_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)