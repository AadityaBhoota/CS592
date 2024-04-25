def largest_subset(a):
    largest_subset = []
    a.sort()
    for num in a:
        if all(num % x == 0 for x in largest_subset):
            largest_subset.append(num)
    return len(largest_subset)

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)