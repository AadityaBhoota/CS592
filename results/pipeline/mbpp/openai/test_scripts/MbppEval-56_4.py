def rev(num):    
    '''
    Write a python function to check if a given number is one less than twice its reverse.

    Examples:
    check(70) == False
    check(23) == False
    check(73) == True
    '''
def check(num):
    rev_num = int(str(num)[::-1])  # reversing the number
    rev_times_2 = rev_num * 2  # multiplying the reversed number by 2
    
    is_condition_met = num == rev_times_2 - 1
    return is_condition_met

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)