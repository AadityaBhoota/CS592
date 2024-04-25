def remove_Occ(s, ch): 
    '''
    Remove the first and last occurrence of a given character from the string.

    Parameters:
    s (str): Input string
    ch (str): Character to be removed

    Returns:
    str: Updated string after removing first and last occurrences of specified character
    '''
    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)

    if first_occurrence != -1:
        s = s[:first_occurrence] + s[first_occurrence+1:]

        if last_occurrence != first_occurrence:
            s = s[:last_occurrence] + s[last_occurrence+1:]

    return s

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)