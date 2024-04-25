def is_undulating(n):
    if len(str(n)) < 3 or not str(n).isdigit():
        return False

    n_str = str(n)
    for i in range(len(n_str) - 2):
        if not (n_str[i] != n_str[i + 1] and n_str[i + 1] != n_str[i + 2] and n_str[i] != n_str[i + 2]):
            return False
    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)