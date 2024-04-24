def count(lst):
    return sum(1 for item in lst if item is True)

def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3

check(count)