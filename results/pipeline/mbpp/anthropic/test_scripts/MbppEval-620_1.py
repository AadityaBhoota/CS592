def largest_subset(a):
    max_size = 0
    subset = []

    for i in range(1, 2 ** len(a)):
        current_subset = []
        for j in range(len(a)):
            if i & (1 << j):
                current_subset.append(a[j])

        if all(a % b == 0 or b % a == 0 for a in current_subset for b in current_subset):
            if len(current_subset) > max_size:
                max_size = len(current_subset)
                subset = current_subset

    return max_size

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)