def validate(n):
    # Converting the integer to a string to easily access each digit
    num_str = str(n)
    
    # Creating a dictionary to store the frequency of each digit
    digit_freq = {}
    
    for digit in num_str:
        # Incrementing the count of digit in the dictionary
        if digit in digit_freq:
            digit_freq[digit] += 1
        else:
            digit_freq[digit] = 1
    
    # Checking if the frequency of each digit is less than or equal to the digit itself
    for digit in digit_freq:
        if int(digit) < digit_freq[digit]:
            return False
    
    return True

# Testing the function with examples




def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)