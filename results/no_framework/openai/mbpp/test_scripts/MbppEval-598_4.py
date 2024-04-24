def armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_digits = sum([int(digit)**num_digits for digit in num_str])

    return sum_digits == number

# Test cases




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)