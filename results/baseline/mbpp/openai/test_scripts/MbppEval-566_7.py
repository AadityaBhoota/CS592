def sum_digits(n):
    # Initialize sum variable to store the sum of digits
    total = 0
    
    # Loop through the digits of the number
    while n > 0:
        digit = n % 10  # Get the rightmost digit
        total += digit  # Add the digit to the total sum
        n //= 10  # Remove the rightmost digit from the number
    
    return total

# Test cases




def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)