def unique_Element(arr):
    '''
    Check whether a list of numbers contains only one distinct element or not.
    
    Arguments:
    arr -- List of numbers
    
    Returns:
    'YES' if the list contains only one distinct element, 'NO' otherwise
    '''
    unique_elements = set(arr)
    
    if len(unique_elements) == 1:
        return 'YES'
    else:
        return 'NO'

# Test cases
assert unique_Element([1, 1, 1]) == 'YES'
assert unique_Element([1, 2, 1, 2]) == 'NO'
assert unique_Element([1, 2, 3, 4, 5]) == 'NO'

def check(candidate):
    assert unique_Element([1,1,1]) == True
    assert unique_Element([1,2,1,2]) == False
    assert unique_Element([1,2,3,4,5]) == False

check(unique_Element)