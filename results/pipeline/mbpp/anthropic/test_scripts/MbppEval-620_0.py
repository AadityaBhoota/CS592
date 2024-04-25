def largest_subset(a):
    max_size = 0
    for subset in find_subsets(a):
        if is_divisible_subset(subset):
            max_size = max(max_size, len(subset))
    return max_size

def is_divisible_subset(subset):
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            if subset[i] % subset[j] != 0 and subset[j] % subset[i] != 0:
                return False
    return True

def find_subsets(a):
    if not a:
        return [[]]
    subsets = []
    for i in range(len(a)):
        for subset in find_subsets(a[i+1:]):
            subsets.append([a[i]] + subset)
    return subsets + find_subsets(a[1:])

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)