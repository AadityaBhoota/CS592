def rev(num):    
    '''
    Write a python function to check if a given number is one less than twice its reverse.

    Examples:
    check(70) == False
    check(23) == False
    check(73) == True
    '''
def check(num):
    reverse_num = int(str(num)[::-1])
    return num == 2*reverse_num + 1

# Test examples




def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)