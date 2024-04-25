def remove_Occ(s, ch):
    result = ""
    first_occurrence = True
    for c in s:
        if c != ch:
            result += c
        elif c == ch and first_occurrence:
            first_occurrence = False
        elif c == ch and not first_occurrence:
            continue
    return result

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)