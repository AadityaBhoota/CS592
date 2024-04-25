def swap_List(newList): 
    # Check if the list has at least two elements
    if len(newList) < 2:
        return newList
    
    # Swap the first and last elements
    newList[0], newList[-1] = newList[-1], newList[0]
    
    return newList

# Test the function




def check(candidate):
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    assert swap_List([1, 2, 3]) == [3, 2, 1]
    assert swap_List([4, 5, 6]) == [6, 5, 4]

check(swap_List)