from itertools import combinations

def largest_subset(a, k):
    largest_size = 0

    for i in range(1, len(a)+1):
        for subset in combinations(a, i):
            valid_subset = True
            for pair in combinations(subset, 2):
                if pair[0] % pair[1] != 0 and pair[1] % pair[0] != 0:
                    valid_subset = False
                    break
            if valid_subset:
                largest_size = max(largest_size, len(subset))

    return largest_size

# Test cases




def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)