def check_tuplex(tuplex, tuple1):
    '''
    Write a function to check whether an element exists within a tuple.

    Examples:
    check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r') == True
    check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5') == False
    check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3) == True
    '''
    return tuple1 in tuplex

def check(candidate):
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True

check(check_tuplex)