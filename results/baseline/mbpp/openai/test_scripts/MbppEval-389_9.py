def find_lucas(n): 
    if n == 0: 
        return 2
    if n == 1: 
        return 1
    lucas_minus1 = 1
    lucas_minus2 = 2
    
    for i in range(2, n+1): 
        lucas = lucas_minus1 + lucas_minus2
        lucas_minus2 = lucas_minus1
        lucas_minus1 = lucas
    
    return lucas

# Test cases




def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)