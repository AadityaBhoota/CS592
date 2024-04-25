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
    reversed_num = int(num_str[::-1])
    
    twice_reversed = 2 * reversed_num
    
    return num == twice_reversed - 1

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)