import math

def is_polite(n):
    count = 0
    number = 1
    
    # Step 1: Initialize a variable `count` to 0 to keep track of the number of polite numbers found.
    while count < n:
        number += math.floor(number / 2)  # Step 2: Increment number using the polite formula
        
        # Step 3: Check if the incremented number is a polite number
        if number % 2 == 1:
            count += 1  # Step 4: Increment count if the number is a polite number
            
    return number  # Step 5: Return the nth polite number

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)