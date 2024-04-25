def sum_div(number):
    total = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            total += i
            if i != number // i:
                total += number // i
    return total

def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1

check(sum_div)