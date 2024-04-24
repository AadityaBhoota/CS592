def all_Characters_Same(s):
    return all(char == s[0] for char in s)

# Test cases




def check(candidate):
    assert all_Characters_Same("python") == False
    assert all_Characters_Same("aaa") == True
    assert all_Characters_Same("data") == False

check(all_Characters_Same)