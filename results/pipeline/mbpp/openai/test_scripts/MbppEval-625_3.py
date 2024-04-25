def swap_List(newList):
    total_elements = len(newList)
    
    if total_elements >= 2:
        newList[0], newList[-1] = newList[-1], newList[0]

    return newList

def check(candidate):
    assert swap_List([1,2,3]) == [3,2,1]
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
    assert swap_List([4,5,6]) == [6,5,4]

check(swap_List)