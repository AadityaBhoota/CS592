def check_Consecutive(l): 
    sorted_list = sorted(l)
    for i in range(len(sorted_list)-1):
        if sorted_list[i+1] - sorted_list[i] != 1:
            return False
    return True

# Test cases




def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False

check(check_Consecutive)