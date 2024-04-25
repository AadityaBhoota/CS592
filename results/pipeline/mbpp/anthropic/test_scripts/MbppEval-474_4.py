def replace_char(str1, ch, newch):
    result = ""
    for c in str1:
        if c == ch:
            result += newch
        else:
            result += c
    return result

def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")

check(replace_char)