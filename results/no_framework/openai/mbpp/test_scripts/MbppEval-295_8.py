def sum_div(number):
    div_sum = 0
    for i in range(1, number):
        if number % i == 0:
            div_sum += i
    return div_sum

# Test the function




def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1

check(sum_div)