import re

def replace_specialchar(text):
    """
    Write a function to replace all occurrences of spaces, commas, or dots with a colon.

    Examples:
    replace_specialchar('Python language, Programming language.') == ('Python:language::Programming:language:')
    replace_specialchar('a b c,d e f') == ('a:b:c:d:e:f')
    replace_specialchar('ram reshma,ram rahim') == ('ram:reshma:ram:rahim')
    """
    return re.sub(r'[ ,.]', ':', text)

def check(candidate):
    assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
    assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')
    assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')

check(replace_specialchar)