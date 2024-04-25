def rev(num):
    """
    Write a python function to check if a given number is one less than twice its reverse.

    Examples:
    rev(70) == False
    rev(23) == False
    rev(73) == True
    """
    # Convert the number to a string and reverse it
    reverse_num = int(str(num)[::-1])
    
    # Check if the given number is one less than twice its reverse
    return num == 2 * reverse_num - 1

# Test cases




def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)