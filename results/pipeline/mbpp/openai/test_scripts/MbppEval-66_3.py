def pos_count(lst):
    count = 0

    for num in lst:
        if num > 0:
            count += 1

    return count

def check(candidate):
    assert pos_count([1,-2,3,-4]) == 2
    assert pos_count([3,4,5,-1]) == 3
    assert pos_count([1,2,3,4]) == 4

check(pos_count)