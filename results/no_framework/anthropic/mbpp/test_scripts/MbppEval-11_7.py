def remove_Occ(s, ch):
    """
    Write a python function to remove first and last occurrence of a given character from the string.

    Examples:
    remove_Occ("hello","l") == "heo"
    remove_Occ("abcda","a") == "bcd"
    remove_Occ("PHP","P") == "H"
    """
    if not s:
        return s

    first_idx = s.find(ch)
    if first_idx == -1:
        return s

    last_idx = s.rfind(ch)
    if first_idx == last_idx:
        return s[:first_idx] + s[first_idx+1:]
    else:
        return s[:first_idx] + s[first_idx+1:last_idx] + s[last_idx+1:]

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)