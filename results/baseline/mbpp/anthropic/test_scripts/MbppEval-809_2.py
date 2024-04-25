def check_smaller(test_tup1, test_tup2):
    '''
    Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.

    Examples:
    check_smaller((1, 2, 3), (2, 3, 4)) == False
    check_smaller((4, 5, 6), (3, 4, 5)) == True
    check_smaller((11, 12, 13), (10, 11, 12)) == True
    '''
    if len(test_tup1) != len(test_tup2):
        return False

    for i in range(len(test_tup1)):
        if test_tup1[i] <= test_tup2[i]:
            return False

    return True

def check(candidate):
    assert check_smaller((1, 2, 3), (2, 3, 4)) == False
    assert check_smaller((4, 5, 6), (3, 4, 5)) == True
    assert check_smaller((11, 12, 13), (10, 11, 12)) == True

check(check_smaller)