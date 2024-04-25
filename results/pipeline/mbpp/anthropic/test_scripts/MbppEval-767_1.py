def get_pairs_count(arr, target_sum):
    count = 0
    seen = {}

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += seen[complement]
        seen[num] = seen.get(num, 0) + 1

    return count

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)