def remove_Occ(s, ch):
    """
    Write a python function to remove first and last occurrence of a given character from the string.

    Examples:
    remove_Occ("hello", "l") == "heo"
    remove_Occ("abcda", "a") == "bcd"
    remove_Occ("PHP", "P") == "H"
    """
    if s.count(ch) < 2:
        return s.replace(ch, "")
    else:
        first_index = s.index(ch)
        last_index = s.rindex(ch)
        return s[:first_index] + s[first_index+1:last_index] + s[last_index+1:]

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)