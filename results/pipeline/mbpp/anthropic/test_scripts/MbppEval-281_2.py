def all_unique(test_list):
    """
    Write a python function to check if the elements of a given list are unique or not.

    Examples:
    all_unique([1,2,3]) == True
    all_unique([1,2,1,2]) == False
    all_unique([1,2,3,4,5]) == True
    """
    unique_elements = set()
    for item in test_list:
        unique_elements.add(item)
    return len(unique_elements) == len(test_list)

def check(candidate):
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,1,2]) == False
    assert all_unique([1,2,3,4,5]) == True

check(all_unique)