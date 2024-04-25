def check_Consecutive(l):
    if len(l) == 0:
        return False
    
    l.sort()
    for i in range(1, len(l)):
        if l[i] != l[i-1] + 1:
            return False
        
    return True

# Test cases




def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False

check(check_Consecutive)