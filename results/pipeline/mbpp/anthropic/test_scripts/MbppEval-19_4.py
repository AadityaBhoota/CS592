def test_duplicate(arraynums):
    unique_set = set(arraynums)
    return len(unique_set) != len(arraynums)

def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

check(test_duplicate)