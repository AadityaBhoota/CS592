def armstrong_number(number):
    total = 0
    num_str = str(number)
    
    num_digits = len(num_str)
    
    for digit in num_str:
        total += int(digit) ** num_digits
    
    return total == number

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)