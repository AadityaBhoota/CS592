def jacobsthal_num(n): 
    if n <= 0:  
        return None
    
    a, b = 0, 1  
    
    if n == 1 or n == 2:  
        return a if n == 1 else b
    
    for _ in range(3, n + 1):  
        c = a + 2 * b  
        a, b = b, c  
        
    return c  

def check(candidate):
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(2) == 1
    assert jacobsthal_num(4) == 5
    assert jacobsthal_num(13) == 2731

check(jacobsthal_num)