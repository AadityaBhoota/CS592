def diff_even_odd(list1):
    first_even = None
    first_odd = None
    
    for num in list1:
        if num % 2 == 0 and first_even is None:
            first_even = num
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
    
    if first_even is not None and first_odd is not None:
        return abs(first_even - first_odd)
    else:
        return 0

def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)