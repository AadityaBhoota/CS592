def largest_subset(a):
    max_size = 0
    current_subset = []
    
    for num in a:
        can_add = True
        for subset_num in current_subset:
            if num % subset_num != 0 and subset_num % num != 0:
                can_add = False
                break
        
        if can_add:
            current_subset.append(num)
            if len(current_subset) > max_size:
                max_size = len(current_subset)
        else:
            current_subset = [num]
    
    return max_size

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)