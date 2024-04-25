def sum_Of_Subarray_Prod(arr):
    """
    Write a python function to find the sum of products of all possible sublists of a given list.

    Examples:
    sum_Of_Subarray_Prod([1,2,3], 3) == 20
    sum_Of_Subarray_Prod([1,2], 2) == 5
    sum_Of_Subarray_Prod([1,2,3,4], 4) == 84
    """
    n = len(arr)
    total_sum = 0

    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= arr[k]
            total_sum += product

    return total_sum

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)