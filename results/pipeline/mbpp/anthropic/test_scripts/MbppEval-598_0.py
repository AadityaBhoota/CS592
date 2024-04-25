def armstrong_number(number):
    """
    Write a function to check whether the given number is armstrong or not.

    Examples:
    armstrong_number(153) == True
    armstrong_number(259) == False
    armstrong_number(4458) == False
    """
    num_str = str(number)
    sum_of_cubes = 0
    for digit in num_str:
        sum_of_cubes += int(digit) ** len(num_str)
    return sum_of_cubes == number

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)