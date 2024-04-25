def first_Digit(n):
    # Step 0: Convert the number to a string
    n_str = str(n)
    
    # Step 1: Get the first character of the string
    first_char = n_str[0]
    
    # Step 2: Convert the first character back to an integer
    first_digit = int(first_char)
    
    # Step 3: Return the integer value
    return first_digit

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)