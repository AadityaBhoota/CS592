def armstrong_number(number):
    # Calculate the number of digits in the given number
    num_digits = len(str(number))
    
    # Calculate the sum of the nth power of each digit in the number
    sum_of_powers = sum(int(digit)**num_digits for digit in str(number))
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Test the function with examples




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)