def armstrong_number(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit)**power for digit in num_str)
    
    return total == number

# Test cases




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)