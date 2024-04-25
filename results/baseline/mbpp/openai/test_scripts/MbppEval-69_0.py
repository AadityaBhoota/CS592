def is_sublist(l, s):
    if not s:
        return True
    if not l:
        return False
    if l[:len(s)] == s:
        return True
    return is_sublist(l[1:], s)

def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)