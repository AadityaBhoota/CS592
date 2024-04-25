def pos_count(list_of_numbers):
    positive_count = 0
    for num in list_of_numbers:
        if num > 0:
            positive_count += 1
    return positive_count

def check(candidate):
    assert pos_count([1,-2,3,-4]) == 2
    assert pos_count([3,4,5,-1]) == 3
    assert pos_count([1,2,3,4]) == 4

check(pos_count)