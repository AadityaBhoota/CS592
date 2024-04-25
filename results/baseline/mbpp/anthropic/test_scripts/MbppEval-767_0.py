def get_pairs_count(arr, target_sum):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                count += 1
    return count

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)