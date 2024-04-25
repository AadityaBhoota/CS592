def mul_even_odd(list1):
    even_prod = None
    odd_prod = None
    
    for num in list1:
        if num % 2 == 0 and even_prod is None:
            even_prod = num
        elif num % 2 != 0 and odd_prod is None:
            odd_prod = num
        
        if even_prod is not None and odd_prod is not None:
            break
            
    return even_prod * odd_prod

def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)