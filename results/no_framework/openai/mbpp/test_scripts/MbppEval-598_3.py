def armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum = 0

    for digit in num_str:
        sum += int(digit) ** num_digits

    return sum == number

# Testing the function with examples




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)