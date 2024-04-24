def replace_blank(str1, char):
    """
    Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.

    Examples:
    replace_blank("hello people", '@') == "hello@people"
    replace_blank("python program language", '$') == "python$program$language"
    replace_blank("blank space", "-") == "blank-space"
    """
    return str1.replace(' ', char)

def check(candidate):
    assert replace_blank("hello people",'@')==("hello@people")
    assert replace_blank("python program language",'$')==("python$program$language")
    assert replace_blank("blank space","-")==("blank-space")

check(replace_blank)