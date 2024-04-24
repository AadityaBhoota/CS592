def amicable_numbers_sum(limit):
    def sum_divisors(n):
        div_sum = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                div_sum += i
                if n // i != i:
                    div_sum += n // i
        return div_sum

    amicable_sum = 0
    for num in range(1, limit + 1):
        sum_num = sum_divisors(num)
        if sum_divisors(sum_num) == num and sum_num != num:
            amicable_sum += num

    return amicable_sum

# Test cases




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)