def remove_Occ(s, ch):
    # Find the index of the first occurrence of the character
    first_occ = s.find(ch)
    if first_occ != -1:  # If character is found
        # Find the index of the last occurrence of the character
        last_occ = s.rfind(ch)
        if last_occ != -1:  # If character is found
            # Remove both the first and last occurrence of the character
            result = s[:first_occ] + s[first_occ+1:last_occ] + s[last_occ+1:]
            return result
    return s

# Test cases




def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)