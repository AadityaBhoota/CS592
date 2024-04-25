def jacobsthal_num(n): 
    if n <= 0:
        return None
        
    a, b = 0, 1
    
    for _ in range(1, n):
        jacobsthal = b + 2*a
        a, b = b, jacobsthal
        
    return jacobsthal

def check(candidate):
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(2) == 1
    assert jacobsthal_num(4) == 5
    assert jacobsthal_num(13) == 2731

check(jacobsthal_num)