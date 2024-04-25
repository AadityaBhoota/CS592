import itertools

def largest_subset(numbers):
    def is_divisible(a, b):
        if a % b == 0 or b % a == 0:
            return True
        return False

    subset_size = 0

    for i in range(1, len(numbers)+1):
        for subset in itertools.combinations(numbers, i):
            valid_subset = all(is_divisible(x, y) for x, y in itertools.combinations(subset, 2))
            if valid_subset and len(subset) > subset_size:
                subset_size = len(subset)

    return subset_size

# Test the function


def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)