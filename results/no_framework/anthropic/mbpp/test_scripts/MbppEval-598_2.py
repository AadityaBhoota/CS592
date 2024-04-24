def armstrong_number(number):
    """
    Write a function to check whether the given number is armstrong or not.

    Examples:
    armstrong_number(153) == True
    armstrong_number(259) == False
    armstrong_number(4458) == False
    """
    # Convert the number to a string to iterate over its digits
    number_str = str(number)
    
    # Initialize the sum of cubes of digits
    sum_of_cubes = 0
    
    # Iterate over each digit and add the cube of the digit to the sum
    for digit in number_str:
        sum_of_cubes += int(digit) ** len(number_str)
    
    # Check if the sum of cubes is equal to the original number
    return sum_of_cubes == number

def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)