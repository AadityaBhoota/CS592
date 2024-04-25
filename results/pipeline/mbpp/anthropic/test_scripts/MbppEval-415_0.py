def max_Product(arr):
    if not arr:
        return (None, None)
    if len(arr) == 1:
        return (arr[0], arr[0])

    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    min1 = min(arr[0], arr[1])
    min2 = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        num = arr[i]
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

    if max1 * max2 >= min1 * min2:
        return (max1, max2)
    else:
        return (min1, min2)

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)