def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    result = 0
    running_product = 1
    for i in range(n):
        running_product *= arr[i]
        result += running_product
    return result

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)