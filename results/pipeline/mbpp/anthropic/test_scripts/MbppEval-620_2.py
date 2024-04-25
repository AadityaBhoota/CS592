def largest_subset(a):
    a.sort()
    subset = [a[0]]
    max_size = 1

    for i in range(1, len(a)):
        if all(a[i] % num == 0 or num % a[i] == 0 for num in subset):
            subset.append(a[i])
            max_size = max(max_size, len(subset))

    return max_size

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)