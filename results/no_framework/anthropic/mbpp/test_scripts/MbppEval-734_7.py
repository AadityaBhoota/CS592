def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            total += product

    return total

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)