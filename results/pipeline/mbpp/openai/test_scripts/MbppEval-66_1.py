def pos_count(lst):
    count = 0  # Step 0

    for num in lst:  # Step 1
        if num > 0:  # Step 2
            count += 1  # Step 3

    return count  # Step 4

def check(candidate):
    assert pos_count([1,-2,3,-4]) == 2
    assert pos_count([3,4,5,-1]) == 3
    assert pos_count([1,2,3,4]) == 4

check(pos_count)