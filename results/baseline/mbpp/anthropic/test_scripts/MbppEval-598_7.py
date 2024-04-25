def armstrong_number(number):
    """
    Write a function to check whether the given number is an Armstrong number or not.

    An Armstrong number is a number that is equal to the sum of the cubes of its digits.

    Examples:
    armstrong_number(153) == True
    armstrong_number(259) == False
    armstrong_number(4458) == False
    """
    # Convert the number to a string to iterate over its digits
    num_str = str(number)

    # Initialize the sum of cubes of digits
    sum_of_cubes = 0

    # Iterate over the digits and add the cube of each digit to the sum
    for digit in num_str:
        sum_of_cubes += int(digit) ** len(num_str)

    # Check if the sum of cubes is equal to the original number
    return sum_of_cubes == number

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)