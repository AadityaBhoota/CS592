def get_pairs_count(arr, count, target_sum):
    pair_count = 0
    
    for i in range(count):
        for j in range(i + 1, count):
            if arr[i] + arr[j] == target_sum:
                pair_count += 1
    
    return pair_count

# Test cases




def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)