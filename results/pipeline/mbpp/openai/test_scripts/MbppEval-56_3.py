def rev(num):    
    '''
    Write a python function to check if a given number is one less than twice its reverse.

    Examples:
    check(70) == False
    check(23) == False
    check(73) == True
    '''
def check(num):    
    num_str = str(num)
    
    # Reverse the string
    reversed_num_str = num_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_num_str)
    
    # Check if the given number is one less than twice its reverse
    if num == 2*reversed_num + 1:
        return True
    else:
        return False

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)