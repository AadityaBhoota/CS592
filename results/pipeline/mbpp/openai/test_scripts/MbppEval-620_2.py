def largest_subset(a):
    max_subset_size = 0
    
    for i in range(len(a)):
        subset = set([a[i])
        
        for j in range(i + 1, len(a)):
            if all([a[j] % num == 0 for num in subset]):
                subset.add(a[j])
        
        max_subset_size = max(max_subset_size, len(subset))
    
    return max_subset_size

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)