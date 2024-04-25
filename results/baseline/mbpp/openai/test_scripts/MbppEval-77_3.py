def is_Diff(n): 
    # Convert the number to a string
    n_str = str(n)
    
    # Calculate the difference between the sum of digits at even positions and odd positions
    diff = sum([int(n_str[i]) for i in range(len(n_str)) if i % 2 == 0]) - sum([int(n_str[i]) for i in range(len(n_str)) if i % 2 != 0])
    
    # Check if the difference is divisible by 11
    if diff % 11 == 0:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)