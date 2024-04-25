def count(lst):   
    count_true = 0
    
    for element in lst:
        if element == True:
            count_true += 1
    
    return count_true

def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3

check(count)