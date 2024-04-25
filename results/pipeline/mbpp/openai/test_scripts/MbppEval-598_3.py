def armstrong_number(number):
    num_str = str(number)  # Convert number to a string

    total = 0
    for digit in num_str:
        digit_int = int(digit)
        total += digit_int ** len(num_str)

    if total == number:
        return True
    else:
        return False

# Testing the function




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)