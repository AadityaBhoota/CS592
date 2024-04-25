def split_Arr(l, n, index):
    """
    Splits a list at the nth element and adds the first part to the end.
    
    Args:
    l (list): The input list to be split.
    n (int): The length of the list.
    index (int): The index at which to split the list.
    
    Returns:
    list: The modified list.
    """
    # Split the list at the given index
    first_part = l[:index]
    second_part = l[index:]
    
    # Concatenate the second part and the first part
    return second_part + first_part

def check(candidate):
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

check(split_Arr)