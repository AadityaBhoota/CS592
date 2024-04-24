def remove_Occ(s, ch):
    first_occ = s.find(ch)
    last_occ = s.rfind(ch)
    if first_occ != -1 and last_occ != -1:
        return s[:first_occ] + s[first_occ+1:last_occ] + s[last_occ+1:]
    else:
        return s

# Test cases




def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)