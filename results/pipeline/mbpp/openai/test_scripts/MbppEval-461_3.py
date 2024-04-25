def upper_ctr(str):
    '''
    Write a python function to count the upper case characters in a given string.
    
    Args:
    str (str): Input string
    
    Returns:
    int: Count of uppercase characters in the input string
    '''
    count = 0  # Initialize count to 0
    
    for char in str:
        if char.isupper():
            count += 1  # Increment count if character is uppercase
    
    return count  # Return the count of uppercase characters

# Test the upper_ctr function




def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0

check(upper_ctr)