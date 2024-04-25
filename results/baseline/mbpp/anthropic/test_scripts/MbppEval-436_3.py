def neg_nos(list1):
    '''
    Write a python function to return the negative numbers in a list.

    Examples:
    neg_nos([-1,4,5,-6]) == "-1,-6"
    neg_nos([-1,-2,3,4]) == "-1,-2"
    neg_nos([-7,-6,8,9]) == "-7,-6"
    '''
    negative_numbers = [str(num) for num in list1 if num < 0]
    return ','.join(negative_numbers)

def check(candidate):
    assert neg_nos([-1,4,5,-6]) == [-1,-6]
    assert neg_nos([-1,-2,3,4]) == [-1,-2]
    assert neg_nos([-7,-6,8,9]) == [-7,-6]

check(neg_nos)