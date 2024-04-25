def replace_blank(str1, char):
    # Step 2: Replace blank spaces in the string with the character
    replaced_str = str1.replace(' ', char)
    return replaced_str

def check(candidate):
    assert replace_blank("hello people",'@')==("hello@people")
    assert replace_blank("python program language",'$')==("python$program$language")
    assert replace_blank("blank space","-")==("blank-space")

check(replace_blank)