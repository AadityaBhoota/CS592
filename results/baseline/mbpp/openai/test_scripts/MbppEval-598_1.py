def armstrong_number(number):
    # Calculate the number of digits in the given number
    num_digits = len(str(number))
    
    # Compute Armstrong sum
    armstrong_sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_digits
        temp //= 10
    
    # Check if the number is an Armstrong number
    return armstrong_sum == number

# Test cases




def check(candidate):
    assert armstrong_number(153)==True
    assert armstrong_number(259)==False
    assert armstrong_number(4458)==False

check(armstrong_number)