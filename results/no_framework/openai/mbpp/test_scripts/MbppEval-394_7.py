def check_distinct(test_tup):
    if len(test_tup) == len(set(test_tup)):
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True

check(check_distinct)