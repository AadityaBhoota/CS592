def mul_even_odd(list1):
    even_found = False
    odd_found = False
    product = 1
    
    for num in list1:
        if not even_found and num % 2 == 0:
            product *= num
            even_found = True
        elif not odd_found and num % 2 == 1:
            product *= num
            odd_found = True
        
        if even_found and odd_found:
            break
    
    return product

# Testing the function with the given examples




def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)