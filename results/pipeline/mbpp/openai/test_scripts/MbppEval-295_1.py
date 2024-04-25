def sum_div(number):
    sum_of_divisors = 0

    for i in range(1, number + 1):
        if number % i == 0:
            sum_of_divisors += i

    return sum_of_divisors

def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1

check(sum_div)