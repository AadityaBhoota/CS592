# Final implementation of the all_Characters_Same function

def all_Characters_Same(s):
    if len(s) < 2:
        return True
    for i in range(1, len(s)):
        if s[i] != s[0]:
            return False
    return True

# Test cases




def check(candidate):
    assert all_Characters_Same("python") == False
    assert all_Characters_Same("aaa") == True
    assert all_Characters_Same("data") == False

check(all_Characters_Same)