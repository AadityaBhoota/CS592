def mul_even_odd(list1):
    """
    Write a function to find the product of first even and odd number of a given list.

    Examples:
    mul_even_odd([1,3,5,7,4,1,6,8]) == 4
    mul_even_odd([1,2,3,4,5,6,7,8,9,10]) == 2
    mul_even_odd([1,5,7,9,10]) == 10
    """
    even = None
    odd = None

    for num in list1:
        if even is None and num % 2 == 0:
            even = num
        if odd is None and num % 2 != 0:
            odd = num
        if even is not None and odd is not None:
            break

    if even is None or odd is None:
        return 0
    else:
        return even * odd

def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)