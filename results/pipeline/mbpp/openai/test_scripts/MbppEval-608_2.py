def bell_Number(n): 
    '''
    Write a python function to find nth bell number.

    Examples:
    bell_Number(2) == 2
    bell_Number(3) == 5
    bell_Number(4) == 15
    '''
    return bell_triangle[n][-1]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)