def sum_digits(n):
    sum_digits = 0
    
    n_str = str(n)
    
    sum_digits = 0
    
    for digit in n_str:
        sum_digits += int(digit)
    
    return sum_digits

def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)