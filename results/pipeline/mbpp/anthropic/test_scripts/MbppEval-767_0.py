def get_pairs_count(arr, target_sum):
    count = 0
    element_counts = {}

    for num in arr:
        if target_sum - num in element_counts:
            count += element_counts[target_sum - num]
        element_counts[num] = element_counts.get(num, 0) + 1

    return count

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)