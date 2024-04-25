def sum_divisors(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

def amicable_numbers_sum(limit):
    total_sum = 0
    for num in range(1, limit + 1):
        sum_of_divisors = sum_divisors(num)
        if sum_of_divisors != num and sum_divisors(sum_of_divisors) == num:
            total_sum += num
    return total_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)