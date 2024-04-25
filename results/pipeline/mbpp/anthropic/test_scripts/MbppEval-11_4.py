def remove_Occ(s, ch):
    first_idx = s.find(ch)
    last_idx = s.rfind(ch)

    if first_idx == -1:
        return s

    return s[:first_idx] + s[first_idx+1:last_idx] + s[last_idx+1:]

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)