def get_pairs_count(arr, sum):
    count = 0
    num_dict = {}
    
    for num in arr:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    for num in arr:
        diff = sum - num
        if diff in num_dict and num_dict[diff] > 0:
            count += num_dict[diff]
        
        if num != diff:
            num_dict[num] -= 1
    
    return count

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)