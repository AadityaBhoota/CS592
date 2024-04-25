def is_happy(s):
    """
    You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    """
    if len(s) < 3:
        return False

    unique_letters = set(s[:3])
    if len(unique_letters) < 3:
        return False

    for i in range(3, len(s)):
        unique_letters.remove(s[i-3])
        unique_letters.add(s[i])
        if len(unique_letters) < 3:
            return False

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