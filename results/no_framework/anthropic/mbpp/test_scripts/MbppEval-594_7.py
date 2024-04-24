def diff_even_odd(list1):
    """
    Write a function to find the difference of the first even and first odd number of a given list.

    Examples:
    diff_even_odd([1,3,5,7,4,1,6,8]) == 3
    diff_even_odd([1,2,3,4,5,6,7,8,9,10]) == 1
    diff_even_odd([1,5,7,9,10]) == 9
    """
    first_even = None
    first_odd = None

    for num in list1:
        if first_even is None and num % 2 == 0:
            first_even = num
        elif first_odd is None and num % 2 != 0:
            first_odd = num

        if first_even is not None and first_odd is not None:
            break

    if first_even is None:
        first_even = float('inf')
    if first_odd is None:
        first_odd = float('inf')

    return abs(first_even - first_odd)

def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)