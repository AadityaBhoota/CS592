def max_Product(arr):
    if len(arr) < 2:
        return "Array must have at least 2 elements"

    max_val = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])
    min_val = min(arr[0], arr[1])
    second_min = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > max_val:
            second_max = max_val
            max_val = arr[i]
        elif arr[i] > second_max:
            second_max = arr[i]
        
        if arr[i] < min_val:
            second_min = min_val
            min_val = arr[i]
        elif arr[i] < second_min:
            second_min = arr[i]
    
    if max_val * second_max > min_val * second_min:
        return (second_max, max_val)
    else:
        return (second_min, min_val)

# Test cases




def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)