def remove_Occ(s, ch):
    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)

    if first_occurrence != -1 and last_occurrence != -1:
        return s[:first_occurrence] + s[first_occurrence+1:last_occurrence] + s[last_occurrence+1:]
    else:
        return s

# Test cases




def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)