def count(lst):
    true_count = 0
    for element in lst:
        if element:
            true_count += 1
    return true_count

def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3

check(count)