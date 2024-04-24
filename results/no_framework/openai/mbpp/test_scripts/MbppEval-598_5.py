def armstrong_number(number):
    num_str = str(number)
    num_len = len(num_str)
    armstrong_sum = 0

    for digit in num_str:
        armstrong_sum += int(digit) ** num_len

    return armstrong_sum == number

# Test cases




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)