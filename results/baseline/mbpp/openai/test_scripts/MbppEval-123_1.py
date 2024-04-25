def amicable_numbers_sum(limit):
    def sum_of_divisors(n):
        return sum([i for i in range(1, n) if n % i == 0])
    
    amicable_sum = 0

    for num in range(2, limit+1):
        if num in found_amicable:
            continue

        sum_div = sum_of_divisors(num)
        if sum_div != num and sum_of_divisors(sum_div) == num:
            amicable_sum += num + sum_div
            found_amicable.add(sum_div)

    return amicable_sum

# Testing the function with examples




def check(candidate):
    assert amicable_numbers_sum(999)==504
    assert amicable_numbers_sum(9999)==31626
    assert amicable_numbers_sum(99)==0

check(amicable_numbers_sum)