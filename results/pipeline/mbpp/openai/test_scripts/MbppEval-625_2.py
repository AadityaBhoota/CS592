def swap_List(newList):
    first_element = newList[0]
    last_element = newList[-1]
    newList[0] = last_element
    newList[-1] = first_element
    return newList

def check(candidate):
    assert swap_List([1,2,3]) == [3,2,1]
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
    assert swap_List([4,5,6]) == [6,5,4]

check(swap_List)