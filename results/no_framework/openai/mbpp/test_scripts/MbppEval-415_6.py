def max_Product(arr): 
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    min1 = min(arr[0], arr[1])
    min2 = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
        
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]
    
    if max1 * max2 > min1 * min2:
        return (max2, max1)
    else:
        return (min1, min2)

# Test cases




def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)