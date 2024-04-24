def remove_odd(l):
    '''
    Write a python function to remove odd numbers from a given list.

    Examples:
    remove_odd([1,2,3]) == [2]
    remove_odd([2,4,6]) == [2,4,6]
    remove_odd([10,20,3]) == [10,20]
    '''
    return [x for x in l if x % 2 == 0]

def check(candidate):
    assert remove_odd([1,2,3]) == [2]
    assert remove_odd([2,4,6]) == [2,4,6]
    assert remove_odd([10,20,3]) == [10,20]

check(remove_odd)