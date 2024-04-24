def armstrong_number(number):
    num_str = str(number)
    armstrong_sum = 0

    for digit in num_str:
        armstrong_sum += int(digit) ** len(num_str)

    return armstrong_sum == number

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)