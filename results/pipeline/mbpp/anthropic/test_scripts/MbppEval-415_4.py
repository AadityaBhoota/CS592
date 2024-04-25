def max_Product(arr):
    if len(arr) < 2:
        return None
    
    max1 = None
    max2 = None
    
    for num in arr:
        if max1 is None or num > max1:
            max2 = max1
            max1 = num
        elif max2 is None or num > max2:
            max2 = num
    
    return (max1, max2)

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)