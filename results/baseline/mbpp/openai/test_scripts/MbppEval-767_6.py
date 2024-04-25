def get_pairs_count(arr, target_sum):
    pair_count = 0
    num_counts = {}

    for num in arr:
        complement = target_sum - num

        if complement in num_counts:
            pair_count += num_counts[complement]

        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    return pair_count

# Test cases




def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)