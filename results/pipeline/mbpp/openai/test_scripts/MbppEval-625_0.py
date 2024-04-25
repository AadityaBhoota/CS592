def swap_List(newList):
    if len(newList) > 1:
        new_list = newList[:]  # Create a copy of the original list to avoid modifying the input list directly
        new_list[0], new_list[-1] = new_list[-1], new_list[0]  # Swap the first and last elements
        return new_list
    return newList  # Return the original list if its length is 0 or 1

def check(candidate):
    assert swap_List([1,2,3]) == [3,2,1]
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
    assert swap_List([4,5,6]) == [6,5,4]

check(swap_List)