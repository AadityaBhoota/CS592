def amicable_numbers_sum(limit):
    amicable_numbers = set()

    for num in range(1, limit):
        proper_divisors_sum = sum(divisor for divisor in range(1, num) if num % divisor == 0)
        if sum(divisor for divisor in range(1, proper_divisors_sum) if proper_divisors_sum % divisor == 0) == num and num != proper_divisors_sum:
            amicable_numbers.add(num)
            amicable_numbers.add(proper_divisors_sum)

    return sum(amicable_numbers)

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)