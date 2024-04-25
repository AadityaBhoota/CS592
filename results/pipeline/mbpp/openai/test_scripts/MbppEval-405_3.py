def check_tuplex(tuplex, tuple1): 
    found = False
    for i in tuplex:
        if i == tuple1:
            found = True
            break
    return found

def check(candidate):
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True

check(check_tuplex)