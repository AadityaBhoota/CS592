def sum_of_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def amicable_numbers_sum(limit):
    amicable_sum = 0
    for a in range(1, limit + 1):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_sum += a
    return amicable_sum

# Examples




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)