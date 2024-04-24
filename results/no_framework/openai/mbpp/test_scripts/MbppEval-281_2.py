def all_unique(test_list):
    return len(test_list) == len(set(test_list)

# Test cases




def check(candidate):
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,1,2]) == False
    assert all_unique([1,2,3,4,5]) == True

check(all_unique)