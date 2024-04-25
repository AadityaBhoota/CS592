def remove_Occ(s, ch):
    if s.count(ch) < 2:
        return s
    
    first_occ = s.index(ch)
    last_occ = s.rindex(ch)
    
    new_str = s[:first_occ] + s[first_occ+1:last_occ] + s[last_occ+1:]
    
    return new_str

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)