def mul_even_odd(list1):
    even_num = None
    odd_num = None
    
    for num in list1:
        if num % 2 == 0 and even_num is None:
            even_num = num
        elif num % 2 != 0 and odd_num is None:
            odd_num = num
    
    if even_num is not None and odd_num is not None:
        return even_num * odd_num
    else:
        return None

def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)