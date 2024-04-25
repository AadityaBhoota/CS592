def all_Characters_Same(s):
    if len(s) <= 1:
        return True
    else:
        first_char = s[0]
        for char in s[1:]:
            if char != first_char:
                return False
        return True

def check(candidate):
    assert all_Characters_Same("python") == False
    assert all_Characters_Same("aaa") == True
    assert all_Characters_Same("data") == False

check(all_Characters_Same)