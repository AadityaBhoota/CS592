def all_unique(test_list):
    unique_elements = set()
    
    for element in test_list:
        if element in unique_elements:
            return False
        unique_elements.add(element)
    
    return True

def check(candidate):
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,1,2]) == False
    assert all_unique([1,2,3,4,5]) == True

check(all_unique)