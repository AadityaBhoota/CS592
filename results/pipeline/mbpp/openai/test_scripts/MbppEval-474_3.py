def replace_char(str1, ch, newch):
    modified_str = ""
    for char in str1:
        if char == ch:
            modified_str += newch
        else:
            modified_str += char
    return modified_str

def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")

check(replace_char)