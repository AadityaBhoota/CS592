def sum_digits(n):
    # Convert the integer to a string to iterate through its individual digits
    n_str = str(n)
    
    # Initialize a variable to store the sum of digits
    total = 0
    
    # Iterate through each character in the string (each digit)
    for digit in n_str:
        # Convert each digit back to an integer and add it to the total
        total += int(digit)
    
    return total

# Test cases




def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)