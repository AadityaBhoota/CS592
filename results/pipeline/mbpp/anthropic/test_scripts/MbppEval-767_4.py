def get_pairs_count(arr, sum):
    num_count = {}
    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1

    count = 0
    for a in num_count:
        b = sum - a
        if b in num_count:
            count += num_count[a] * num_count[b]

    return count // 2

def check(candidate):
    assert get_pairs_count([1,1,1,1],2) == 6
    assert get_pairs_count([1,5,7,-1,5],6) == 3
    assert get_pairs_count([1,-2,3],1) == 1
    assert get_pairs_count([-1,-2,3],-3) == 1

check(get_pairs_count)