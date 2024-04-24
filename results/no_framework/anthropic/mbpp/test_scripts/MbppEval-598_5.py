def armstrong_number(number):
    """
    Check whether the given number is an Armstrong number or not.

    An Armstrong number is a number that is equal to the sum of the cubes of its digits.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to iterate over its digits
    num_str = str(number)

    # Calculate the sum of the cubes of the digits
    sum_of_cubes = sum(int(digit) ** len(num_str) for digit in num_str)

    # Check if the sum of the cubes is equal to the original number
    return number == sum_of_cubes

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)