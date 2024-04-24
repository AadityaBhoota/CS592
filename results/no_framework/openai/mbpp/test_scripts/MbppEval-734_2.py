from itertools import combinations

def sum_Of_Subarray_Prod(arr):
    result = 0
    for i in range(1, len(arr)+1):
        for sublist in combinations(arr, i):
            prod = 1
            for num in sublist:
                prod *= num
            result += prod
    return result

# Test cases




def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)