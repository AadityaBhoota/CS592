def armstrong_number(number):
    # Calculate the number of digits in the given number
    num_digits = len(str(number))
    
    # Calculate the sum of each digit raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in str(number))
    
    # Check if the calculated total is equal to the original number
    return total == number

# Test cases




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)