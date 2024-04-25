def replace_char(str1, ch, newch):
    new_str = ""
    for c in str1:
        if c == ch:
            new_str += newch
        else:
            new_str += c
    return new_str

def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")

check(replace_char)