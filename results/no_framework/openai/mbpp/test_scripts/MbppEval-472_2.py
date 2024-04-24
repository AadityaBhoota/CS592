def check_Consecutive(l):
    for i in range(len(l)-1):
        if l[i+1] - l[i] != 1:
            return False
    return True

# Test cases




def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False

check(check_Consecutive)