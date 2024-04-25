def largest_subset(a):
    max_subset_size = 0

    for num in a:
        subset_size = 1  # At least one element in the subset
        subset = [num]  # Initialize subset with num

        for i in range(a.index(num) + 1, len(a)):
            if all(a[i] % ele == 0 for ele in subset):
                subset.append(a[i])
                subset_size += 1

        max_subset_size = max(max_subset_size, subset_size)

    return max_subset_size

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)