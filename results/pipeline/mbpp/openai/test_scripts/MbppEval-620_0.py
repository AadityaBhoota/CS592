def largest_subset(a):
    max_subset = 0
    
    for i in range(len(a)):
        subset = set()
        
        subset.add(a[i])
        
        for j in range(i+1, len(a)):
            if a[j] % a[i] == 0 or a[i] % a[j] == 0:
                subset.add(a[j])
        
        max_subset = max(max_subset, len(subset))
    
    return max_subset

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)