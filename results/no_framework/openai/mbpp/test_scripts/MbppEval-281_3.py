def all_unique(test_list):
    unique_set = set(test_list)
    return len(unique_set) == len(test_list)

# Test cases




def check(candidate):
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,1,2]) == False
    assert all_unique([1,2,3,4,5]) == True

check(all_unique)