def frequency(a, x):
    """
    Write a function to count the number of occurrences of a number in a given list.

    Examples:
    frequency([1,2,3],4) == 0
    frequency([1,2,2,3,3,3,4],3) == 3
    frequency([0,1,2,3,1,2],1) == 2
    """
    count = 0
    for element in a:
        if element == x:
            count += 1
    return count

def check(candidate):
    assert frequency([1,2,3], 4) == 0
    assert frequency([1,2,2,3,3,3,4], 3) == 3
    assert frequency([0,1,2,3,1,2], 1) == 2

check(frequency)