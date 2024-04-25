def replace_blank(str1, char):
    result = ''
    for c in str1:
        if c == ' ':
            result += char
        else:
            result += c
    return result

def check(candidate):
    assert replace_blank("hello people",'@')==("hello@people")
    assert replace_blank("python program language",'$')==("python$program$language")
    assert replace_blank("blank space","-")==("blank-space")

check(replace_blank)