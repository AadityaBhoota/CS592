def get_pairs_count(arr, n, target_sum):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target_sum:
                count += 1
    return count

# Test cases




def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)