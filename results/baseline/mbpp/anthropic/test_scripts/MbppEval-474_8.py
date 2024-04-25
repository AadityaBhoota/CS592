def replace_char(str1, ch, newch):
    """
    Write a function to replace characters in a string.

    Examples:
    replace_char("polygon",'y','l') == ("pollgon")
    replace_char("character",'c','a') == ("aharaater")
    replace_char("python",'l','a') == ("python")
    """
    return str1.replace(ch, newch)

def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")

check(replace_char)