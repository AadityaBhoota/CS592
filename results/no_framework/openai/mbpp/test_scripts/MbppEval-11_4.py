def remove_Occ(s, ch):
    try:
        first_idx = s.index(ch)
        last_idx = s.rindex(ch)
        return s[:first_idx] + s[first_idx+1:last_idx] + s[last_idx+1:]
    except ValueError:
        return s

# Test cases




def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)