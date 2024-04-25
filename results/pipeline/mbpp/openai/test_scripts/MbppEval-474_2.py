def replace_char(str1, ch, newch):
    if ch in str1:
        modified_str = str1.replace(ch, newch)
        return modified_str
    else:
        return str1

# Testing the function with example cases




def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")

check(replace_char)