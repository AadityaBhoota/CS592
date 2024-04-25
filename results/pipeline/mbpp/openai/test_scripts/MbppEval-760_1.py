def unique_Element(arr):
    distinct_elements = set(arr)
    if len(distinct_elements) == 1:
        return 'YES'
    else:
        return 'NO'

def check(candidate):
    assert unique_Element([1,1,1]) == True
    assert unique_Element([1,2,1,2]) == False
    assert unique_Element([1,2,3,4,5]) == False

check(unique_Element)