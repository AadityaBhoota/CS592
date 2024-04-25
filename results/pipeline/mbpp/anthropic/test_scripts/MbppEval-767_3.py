def get_pairs_count(arr, sum):
    seen = set()
    count = 0
    for i in arr:
        if sum - i in seen:
            count += 1
        seen.add(i)
    return count

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)