def replace_char(str1, ch, newch):
    """
    Write a function to replace characters in a string.

    Examples:
    replace_char("polygon", 'y', 'l') == "pollgon"
    replace_char("character", 'c', 'a') == "aharaater"
    replace_char("python", 'l', 'a') == "python"
    """
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