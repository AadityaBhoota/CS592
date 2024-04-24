def mul_even_odd(list1):
    even = None
    odd = None
    for num in list1:
        if num % 2 == 0 and even is None:
            even = num
        elif num % 2 != 0 and odd is None:
            odd = num

        if even is not None and odd is not None:
            return even * odd
    return None

# Test cases




def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)