def split_Arr(l, n):
    if not l:
        return "Input list is empty, please provide a non-empty list."
    
    split_idx = n % len(l)
    
    # Split the list at the specified index, reorder, and concatenate
    reordered_list = l[split_idx:] + l[:split_idx]
    
    return reordered_list

def check(candidate):
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

check(split_Arr)