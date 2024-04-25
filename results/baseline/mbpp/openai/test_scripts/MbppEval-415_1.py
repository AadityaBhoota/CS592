def max_Product(arr): 
    arr.sort()
    n = len(arr)

    if (arr[0] * arr[1]) > (arr[n - 2] * arr[n - 1]):
        return arr[:2]
    else:
        return arr[n - 2:]

# Testing the function with the provided examples




def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)