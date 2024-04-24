def amicable_numbers_sum(limit):
    def sum_divisors(n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.extend([i, n // i])
        return sum(divisors)

    amicable_sum = 0
    for num in range(1, limit + 1):
        if num == sum_divisors(sum_divisors(num)) and num != sum_divisors(num):
            amicable_sum += num
    
    return amicable_sum

# Test cases




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)