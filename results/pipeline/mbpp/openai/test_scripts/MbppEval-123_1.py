def amicable_numbers_sum(limit):
    def find_divisors(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors

    def sum_divisors(num):
        return sum(find_divisors(num))

    amicable_sum = 0
    for num in range(1, limit + 1):
        divisor_sum = sum_divisors(num)
        if divisor_sum != num and sum_divisors(divisor_sum) == num:
            amicable_sum += num

    return amicable_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)