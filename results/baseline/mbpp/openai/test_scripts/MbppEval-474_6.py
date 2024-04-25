def replace_char(str1, ch, newch):
    return str1.replace(ch, newch)

# Test cases




def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")

check(replace_char)