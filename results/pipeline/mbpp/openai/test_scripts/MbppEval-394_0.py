def check_distinct(test_tup):
    unique_set = set(test_tup)
    return len(unique_set) == len(test_tup)

def check(candidate):
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True

check(check_distinct)