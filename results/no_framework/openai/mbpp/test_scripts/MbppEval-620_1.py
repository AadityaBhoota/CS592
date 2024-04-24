from itertools import combinations

def is_divisible_pair(num1, num2):
    return num1 % num2 == 0 or num2 % num1 == 0

def largest_subset(a, k):
    max_size = 0
    for r in range(1, len(a) + 1):
        for subset in combinations(a, r):
            if all(is_divisible_pair(x, y) for x, y in combinations(subset, 2)):
                max_size = max(max_size, len(subset))
    return max_size

# Test cases




def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)