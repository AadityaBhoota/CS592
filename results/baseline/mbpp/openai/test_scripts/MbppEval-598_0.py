def armstrong_number(number):
    # Calculate the total number of digits in the given number
    num_len = len(str(number))
    
    # Calculate the sum of each digit raised to the power of total number of digits
    total = sum(int(digit)**num_len for digit in str(number))
    
    # Check if the total is equal to the given number
    if total == number:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)