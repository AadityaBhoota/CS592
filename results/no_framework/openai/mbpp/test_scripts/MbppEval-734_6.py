def sum_Of_Subarray_Prod(arr, n):
    result = 0
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
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