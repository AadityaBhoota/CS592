def armstrong_number(number):
    """
    Write a function to check whether the given number is armstrong or not.

    Examples:
    armstrong_number(153) == True
    armstrong_number(259) == False
    armstrong_number(4458) == False
    """
    # Convert the number to a list of digits
    digits = [int(digit) for digit in str(number)]

    # Calculate the sum of the cubes of the digits
    sum_of_cubes = sum(digit ** len(digits) for digit in digits)

    # Check if the sum is equal to the original number
    return sum_of_cubes == number

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)