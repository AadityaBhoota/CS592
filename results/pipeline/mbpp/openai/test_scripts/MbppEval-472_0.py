def has_duplicates(lst):
    seen = set()
    for x in lst:
        if x in seen:
            return True
        seen.add(x)
    return False

def check_Consecutive(l):
    if len(l) < 2:
        return True
    for i in range(len(l) - 1):
        if l[i] + 1 != l[i + 1]:
            return False
    if has_duplicates(l):
        return False
    return True

def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False

check(check_Consecutive)