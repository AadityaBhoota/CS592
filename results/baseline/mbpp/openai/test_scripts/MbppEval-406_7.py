def find_Parity(x): 
    '''
    Write a python function to find whether the parity of a given number is odd.

    Examples:
    find_Parity(12) == "Even Parity"
    find_Parity(7) == "Odd Parity"
    find_Parity(10) == "Even Parity"
    '''
def find_parity(x):
    if x % 2 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"

# Test cases




def check(candidate):
    assert find_Parity(12) == False
    assert find_Parity(7) == True
    assert find_Parity(10) == False

check(find_Parity)