def rev(num):
    """
    Write a python function to check if a given number is one less than twice its reverse.

    Examples:
    check(70) == False
    check(23) == False
    check(73) == True
    """
    # Convert the number to a string and reverse it
    reversed_num = int(str(num)[::-1])
    
    # Check if the given number is one less than twice its reverse
    if num == 2 * reversed_num - 1:
        return True
    else:
        return False

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)