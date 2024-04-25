def is_happy(s):
    if len(s) < 3:
        return False
    
    unique_chars = set()
    
    for char in s:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    
    return True

def check(candidate):

    # Check some simple cases
    assert candidate("a") == False , "a"
    assert candidate("aa") == False , "aa"
    assert candidate("abcd") == True , "abcd"
    assert candidate("aabb") == False , "aabb"
    assert candidate("adb") == True , "adb"
    assert candidate("xyy") == False , "xyy"
    assert candidate("iopaxpoi") == True , "iopaxpoi"
    assert candidate("iopaxioi") == False , "iopaxioi"

check(is_happy)