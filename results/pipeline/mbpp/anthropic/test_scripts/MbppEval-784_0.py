def mul_even_odd(list1):
    if not list1:
        return 0
    
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
        return first_odd or 0
    elif first_odd is None:
        return first_even or 0
    else:
        return first_even * first_odd

def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)