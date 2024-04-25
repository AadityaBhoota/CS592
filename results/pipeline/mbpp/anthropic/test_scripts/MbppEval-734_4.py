def sum_Of_Subarray_Prod(arr, n):
    total_sum = 0
    product = 1
    
    for i in range(n):
        total_sum += arr[i] * product
        product *= arr[i]
    
    return total_sum

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)