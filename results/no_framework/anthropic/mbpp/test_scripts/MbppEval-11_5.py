def remove_Occ(s, ch):
    """
    Write a python function to remove first and last occurrence of a given character from the string.

    Examples:
    remove_Occ("hello","l") == "heo"
    remove_Occ("abcda","a") == "bcd"
    remove_Occ("PHP","P") == "H"
    """
    # Check if the string is empty or the character is not present in the string
    if not s or ch not in s:
        return s

    # Find the first and last occurrence of the character
    first_index = s.index(ch)
    last_index = s.rindex(ch)

    # Create a new string by slicing the original string
    # and excluding the first and last occurrence of the character
    return s[:first_index] + s[first_index+1:last_index] + s[last_index+1:]

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)