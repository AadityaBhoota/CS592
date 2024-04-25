def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prefix_prod = [1] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_prod[i] = prefix_prod[i - 1] * arr[i - 1]
    
    result = 0
    for i in range(1, n + 1):
        result += (i * (prefix_prod[i] - prefix_prod[i - 1])) * arr[i - 1]
    
    return result

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)