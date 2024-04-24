def max_Product(arr):
    arr.sort()
    if arr[0] > 0 and arr[-1] > 0:
        return arr[-2], arr[-1]
    else:
        if arr[0]*arr[1] > arr[-2]*arr[-1]:
            return arr[0], arr[1]
        else:
            return arr[-2], arr[-1]

# Test cases




def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)