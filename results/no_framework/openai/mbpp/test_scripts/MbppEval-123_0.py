def amicable_numbers_sum(limit):
    def sum_divisors(n):
        divisors = [1]
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors)

    amicable_sum = 0
    for i in range(1, limit + 1):
        if i < sum_divisors(i) and sum_divisors(sum_divisors(i)) == i:
            amicable_sum += i + sum_divisors(i)

    return amicable_sum

# Testing the function with examples




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)