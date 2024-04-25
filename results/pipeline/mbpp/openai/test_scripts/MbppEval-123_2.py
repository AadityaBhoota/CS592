def amicable_numbers_sum(limit):
    def sum_divisors(n):
        divisors_sum = 1
        for i in range(2, n):
            if n % i == 0:
                divisors_sum += i
        return divisors_sum

    total_sum = 0
    for n in range(1, limit + 1):
        sum_div_n = sum_divisors(n)
        sum_div_sum_div_n = sum_divisors(sum_div_n)

        if n != sum_div_n and n == sum_div_sum_div_n:
            total_sum += n

    return total_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)