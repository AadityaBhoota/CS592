def count(lst):
    true_count = 0

    for item in lst:
        if item == True:
            true_count += 1

    return true_count

def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3

check(count)