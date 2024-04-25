def is_sublist(l, s):
    i = 0
    j = 0
    
    while i < len(l):
        if l[i] == s[j]:
            j += 1
            if j == len(s):
                return True
        else:
            j = 0
        i += 1
    
    return False

def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)