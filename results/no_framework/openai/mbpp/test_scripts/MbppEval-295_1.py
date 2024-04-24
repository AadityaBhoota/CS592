def sum_div(number):
    divisors = [1]  # Include 1 as a divisor for all numbers
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)

# Test cases
assert sum_div(8) == 7
assert sum_div(12) == 16
assert sum_div(7) == 1

def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1

check(sum_div)