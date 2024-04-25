def get_pairs_count(arr, sum):
    freq_map = {}
    pairs_count = 0
    
    for num in arr:
        complement = sum - num
        if complement in freq_map:
            pairs_count += freq_map[complement]
        freq_map[num] = freq_map.get(num, 0) + 1

    return pairs_count

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)