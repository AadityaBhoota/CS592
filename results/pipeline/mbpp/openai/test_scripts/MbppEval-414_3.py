def overlapping(list1, list2):
    '''
    Write a python function to check whether any value in a sequence exists in another sequence or not.

    Examples:
    overlapping([1,2,3,4,5],[6,7,8,9]) == False
    overlapping([1,2,3],[4,5,6]) == False
    overlapping([1,4,5],[1,4,5]) == True
    '''
    found_overlap = False
    for elem1 in list1:
        if elem1 in list2:
            found_overlap = True
            break
    return found_overlap

def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True

check(overlapping)