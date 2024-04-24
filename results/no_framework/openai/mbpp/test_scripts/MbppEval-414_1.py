def overlapping(list1, list2):
    for ele in list1:
        if ele in list2:
            return True
    return False

# Test cases




def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True

check(overlapping)