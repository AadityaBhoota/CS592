def split_Arr(lst, length, index):
    if index >= length or index < 0:
        return lst

    return lst[index:] + lst[:index]

# Test the function with the provided examples




def check(candidate):
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

check(split_Arr)