def test_duplicate(arraynums):
    unique_set = set(arraynums)
    
    if len(arraynums) != len(unique_set):
        return True
    else:
        return False

def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

check(test_duplicate)