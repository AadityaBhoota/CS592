def validate(n):
    # Step 1: Define a dictionary to store the frequency of each digit
    digit_freq = {}
    
    # Step 2: Convert the integer 'n' to a string
    n_str = str(n)
    
    # Step 3: Iterate over each digit in the string representation of 'n'
    for digit in n_str:
        # Step 3a: Check if digit is in the dictionary, if yes, increment its frequency
        if digit in digit_freq:
            digit_freq[digit] += 1
        else:
            digit_freq[digit] = 1
        
        # Step 3b: Check if the frequency of digit is greater than the digit itself
        if digit_freq[digit] > int(digit):
            return False
    
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)