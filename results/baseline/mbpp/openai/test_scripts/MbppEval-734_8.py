def sum_Of_Subarray_Prod(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            sublist = arr[i:j]
            product = 1
            for num in sublist:
                product *= num
            total += product
    return total

# Test cases




def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)