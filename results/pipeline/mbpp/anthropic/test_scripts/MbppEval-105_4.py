def count(lst):
    count = 0
    for element in lst:
        if element:
            count += 1
    return count

def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3

check(count)