def sum_div(number):
    total_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            total_sum += i
    
    return total_sum

def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1

check(sum_div)