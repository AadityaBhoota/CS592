def is_sublist(l, s):
    if len(s) == 0:
        return True
    for i in range(len(l)):
        if l[i] == s[0]:  # Check if the current element matches the first element of the sublist
            if l[i:i + len(s)] == s:  # Check if the sublist matches the current slice of the list
                return True
    return False

# Test cases




def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)