def amicable_numbers_sum(limit):
    def sum_of_divisors(n):
        sum_divisors = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                sum_divisors += i
                if i != n // i:
                    sum_divisors += n // i
        return sum_divisors

    amicable_sum = 0
    for num in range(1, limit+1):
        sum_divisors_num = sum_of_divisors(num)
        if sum_divisors_num != num and sum_of_divisors(sum_divisors_num) == num:
            amicable_sum += num

    return amicable_sum

# Test cases




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)