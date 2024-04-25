def sum_Of_Subarray_Prod(arr):
    result = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i, n):
            sublist = arr[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            result += product
    
    return result

# Test cases




def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)