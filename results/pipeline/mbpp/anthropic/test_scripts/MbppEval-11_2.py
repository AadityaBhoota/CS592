def remove_Occ(s, ch):
    result = ""
    
    # Skip the first occurrence of the character
    if s[0] == ch:
        result = s[1:]
    else:
        result = s
    
    # Remove the last occurrence of the character
    last_index = result.rfind(ch)
    if last_index != -1:
        result = result[:last_index] + result[last_index+1:]
    
    return result

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"

check(remove_Occ)