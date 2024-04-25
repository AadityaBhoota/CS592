def frequency(a, x): 
    count = 0
    
    for num in a:
        if num == x:
            count += 1
            
    return count

def check(candidate):
    assert frequency([1,2,3], 4) == 0
    assert frequency([1,2,2,3,3,3,4], 3) == 3
    assert frequency([0,1,2,3,1,2], 1) == 2

check(frequency)