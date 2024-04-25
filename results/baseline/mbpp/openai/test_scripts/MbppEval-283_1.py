def validate(n): 
    # Convert the integer to a string to iterate through individual digits
    n_str = str(n)
    
    # Create a dictionary to store the frequency of each digit
    digit_freq = {}
    
    # Iterate through each digit in the string
    for digit in n_str:
        if digit in digit_freq:
            digit_freq[digit] += 1
        else:
            digit_freq[digit] = 1
    
    # Check if the frequency of each digit is less than or equal to the digit itself
    for digit, freq in digit_freq.items():
        if int(digit) < freq:
            return False
    
    return True

# Test cases




def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)