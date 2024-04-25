def overlapping(list1, list2):
    is_overlapping = False
    for item in list1:
        if item in list2:
            is_overlapping = True
            break
    return is_overlapping

def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True

check(overlapping)