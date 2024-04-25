def sum_Of_Subarray_Prod(arr):
    """
    Finds the sum of products of all possible sublists of a given list.

    Args:
        arr (list): The input list.

    Returns:
        int: The sum of products of all possible sublists.
    """
    n = len(arr)
    result = 0

    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= arr[k]
            result += product

    return result

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)