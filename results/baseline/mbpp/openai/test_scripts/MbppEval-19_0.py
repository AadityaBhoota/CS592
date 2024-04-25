def test_duplicate(arraynums):
    # Convert the input list to a set to remove duplicates
    unique_set = set(arraynums)
    
    # If the sizes of the original list and the set are different, there are duplicates
    return len(arraynums) != len(unique_set)

# Test cases




def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

check(test_duplicate)