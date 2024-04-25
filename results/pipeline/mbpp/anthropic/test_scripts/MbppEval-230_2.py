def replace_blank(str1, char):
    new_str = ""
    for char_in_str in str1:
        if char_in_str == " ":
            new_str += char
        else:
            new_str += char_in_str
    return new_str

def check(candidate):
    assert replace_blank("hello people",'@')==("hello@people")
    assert replace_blank("python program language",'$')==("python$program$language")
    assert replace_blank("blank space","-")==("blank-space")

check(replace_blank)