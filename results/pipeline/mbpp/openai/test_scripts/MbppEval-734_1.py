from itertools import chain, combinations

def subsets(arr):
    return chain.from_iterable(combinations(arr, r) for r in range(len(arr)+1))

def sum_Of_Subarray_Prod(arr):
    total_sum = sum([reduce(lambda x, y: x * y, sub, 1) for sub in subsets(arr)])
    return total_sum

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)