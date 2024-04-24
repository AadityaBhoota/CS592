def test_duplicate(arraynums):
    num_set = set()
    for num in arraynums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

# Test cases




def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

check(test_duplicate)