def sum_of_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return sum(divisors)

def amicable_numbers_sum(limit):
    def is_amicable(n):
        m = sum_of_divisors(n)
        return n != m and n == sum_of_divisors(m)
    
    amicable_sum = 0
    for i in range(1, limit+1):
        if is_amicable(i):
            amicable_sum += i
    
    return amicable_sum

# Test cases




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)