def test_duplicate(arraynums):
    unique_set = set()
    for num in arraynums:
        if num in unique_set:
            return True
        unique_set.add(num)
    return False

def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

check(test_duplicate)