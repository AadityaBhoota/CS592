def is_sublist(l, s):
    if len(s) > len(l):
        return False

    for i in range(len(l) - len(s) + 1):
        sublist = l[i:i+len(s)]
        
        if sublist == s:
            return True
    
    return False

def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)