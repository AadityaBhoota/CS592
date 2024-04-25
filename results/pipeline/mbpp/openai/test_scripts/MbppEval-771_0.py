from collections import deque
def check_expression(exp):
    '''
    Write a function to check if the given expression is balanced or not. 
    Examples:
    check_expression("{()}[{}]") == True
    check_expression("{()}[{]") == False
    check_expression("{()}[{}][]({})") == True
    '''
    return not stack

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)