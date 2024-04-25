def max_Product(arr):
    if not arr:
        return None
    
    max1 = float('-inf')
    max2 = float('-inf')
    min1 = float('inf')
    min2 = float('inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    if min1 * min2 > max1 * max2:
        return (min1, min2)
    else:
        return (max1, max2)

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)