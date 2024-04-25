def check_distinct(test_tup):
    distinct_set = set()

    for elem in test_tup:
        if elem in distinct_set:
            return False
        distinct_set.add(elem)

    return True

def check(candidate):
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True

check(check_distinct)