def get_pairs_count(arr, sum):
    count = 0
    nums = set()
    
    for num in arr:
        complement = sum - num
        if complement in nums:
            count += 1
        nums.add(num)
    
    return count

# Test cases




def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)