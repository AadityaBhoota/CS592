def amicable_numbers_sum(limit):
    total_sum = 0
    
    for n in range(1, limit):
        sum_of_divisors = sum(divisor for divisor in range(1, n) if n % divisor == 0)
        sum_of_divisors_of_divisors = sum(divisor for divisor in range(1, sum_of_divisors) if sum_of_divisors % divisor == 0)
        
        if n == sum_of_divisors_of_divisors and n != sum_of_divisors:
            total_sum += n
    
    return total_sum

def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)