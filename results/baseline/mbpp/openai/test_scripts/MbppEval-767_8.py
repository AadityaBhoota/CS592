def get_pairs_count(arr, sum):
    pair_count = 0
    nums_dict = {}
    
    for num in arr:
        complement = sum - num
        if complement in nums_dict:
            pair_count += nums_dict[complement]
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    
    return pair_count

# Test cases




def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)