def remove_Occ(s, ch):
    """
    Write a python function to remove the first and last occurrence of a given character from the string.

    Examples:
    remove_Occ("hello", "l") == "heo"
    remove_Occ("abcda", "a") == "bcd"
    remove_Occ("PHP", "P") == "H"
    """
    if not s or not ch:
        return s

    # Find the first and last occurrence of the character
    first_index = s.find(ch)
    last_index = s.rfind(ch)

    if first_index == -1:
        # Character not found in the string
        return s
    elif first_index == last_index:
        # Only one occurrence of the character
        return s.replace(ch, "")
    else:
        # Remove the first and last occurrence of the character
        return s[:first_index] + s[first_index+1:last_index] + s[last_index+1:]

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)