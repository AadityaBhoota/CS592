def remove_Occ(s, ch):
    if not s:
        return s

    first_index = s.find(ch)
    last_index = s.rfind(ch)

    if first_index == last_index:
        return s.replace(ch, "", 1)
    else:
        return s[:first_index] + s[first_index+1:last_index] + s[last_index+1:]

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)