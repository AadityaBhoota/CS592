def Split(list): 
    '''
    Write a python function which takes a list of integers and only returns the odd ones.

    Examples:
    Split([1,2,3,4,5,6]) == [1,3,5]
    Split([10,11,12,13]) == [11,13]
    Split([7,8,9,1]) == [7,9,1]
    '''
def split(lst): 
    result = []
    for num in lst:
        if num % 2 != 0:
            result.append(num)
    return result

def check(candidate):
    assert Split([1,2,3,4,5,6]) == [1,3,5]
    assert Split([10,11,12,13]) == [11,13]
    assert Split([7,8,9,1]) == [7,9,1]

check(Split)