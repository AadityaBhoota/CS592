import re

def replace_specialchar(text):
    # Define a regular expression pattern to match spaces, commas, or dots
    pattern = r'[ ,.]'
    
    # Replace all occurrences of spaces, commas, or dots with a colon
    updated_text = re.sub(pattern, ':', text)
    
    return updated_text

# Test the function with examples




def check(candidate):
    assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
    assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')
    assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')

check(replace_specialchar)