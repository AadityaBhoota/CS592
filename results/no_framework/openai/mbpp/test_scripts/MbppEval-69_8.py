def is_sublist(l, s):
    if not s:
        return True
    
    i = 0
    while i < len(l):
        if l[i] == s[0]:
            if len(l) - i < len(s):
                return False
            
            j = 1
            while j < len(s) and l[i+j] == s[j]:
                j += 1
            
            if j == len(s):
                return True
        
        i += 1
    
    return False

# Test cases




def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)