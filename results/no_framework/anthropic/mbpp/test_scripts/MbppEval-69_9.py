def is_sublist(l, s):
    """
    Write a function to check whether a list contains the given sublist or not.

    Examples:
    is_sublist([2,4,3,5,7],[3,7]) == False
    is_sublist([2,4,3,5,7],[4,3]) == True
    is_sublist([2,4,3,5,7],[1,6]) == False
    """
    return any(s == l[i:i+len(s)] for i in range(len(l)-len(s)+1))

def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)