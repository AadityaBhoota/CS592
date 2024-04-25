def rev(num):
    '''
    Write a python function to check if a given number is one less than twice its reverse.

    Examples:
    check(70) == False
    check(23) == False
    check(73) == True
    '''
    original_num = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original_num == 2 * reversed_num - 1

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)