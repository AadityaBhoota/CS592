def get_pairs_count(arr, sum):
    pair_count = 0

    for i in range(len(arr)):
        diff = sum - arr[i]

        for j in range(i + 1, len(arr)):
            if arr[j] == diff:
                pair_count += 1

    return pair_count

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)