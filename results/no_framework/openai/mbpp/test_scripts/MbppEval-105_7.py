def count(lst):
    return lst.count(True)
    
# Test the function




def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3

check(count)