def replace_blank(str1, char):
    modified_str = str1.replace(' ', char)
    return modified_str

# Test cases




def check(candidate):
    assert replace_blank("hello people",'@')==("hello@people")
    assert replace_blank("python program language",'$')==("python$program$language")
    assert replace_blank("blank space","-")==("blank-space")

check(replace_blank)