def is_sublist(l, s):
    # Convert the input lists to strings for easy comparison
    str_l = ' '.join(map(str, l))
    str_s = ' '.join(map(str, s))

    # Check if the sublist is present in the list
    if str_s in str_l:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)