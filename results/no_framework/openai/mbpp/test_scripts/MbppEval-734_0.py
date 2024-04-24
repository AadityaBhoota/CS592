from itertools import combinations
from numpy import prod

def sum_Of_Subarray_Prod(arr):
    total = 0
    for r in range(1, len(arr) + 1):
        for subset in combinations(arr, r):
            total += prod(subset)
    return total

# Test cases




def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)