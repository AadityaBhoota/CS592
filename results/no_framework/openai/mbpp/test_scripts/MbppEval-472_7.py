def check_Consecutive(l):
    return all(x == y - 1 for x, y in zip(l, l[1:]))

# Test cases




def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False

check(check_Consecutive)