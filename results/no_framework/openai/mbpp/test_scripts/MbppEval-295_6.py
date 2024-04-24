def sum_div(number):
    sum_of_divisors = 1  # 1 is a divisor for all numbers
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            sum_of_divisors += i
            if i != number // i:  # Avoid counting squares twice
                sum_of_divisors += number // i
    return sum_of_divisors

# Test cases




def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1

check(sum_div)