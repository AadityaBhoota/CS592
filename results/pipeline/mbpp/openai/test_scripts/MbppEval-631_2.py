def replace_spaces(text):
    modified_text = ''
    for char in text:
        if char == ' ':
            modified_text += '_'
        elif char == '_':
            modified_text += ' '
        else:
            modified_text += char
    return modified_text

def check(candidate):
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert replace_spaces('The_Avengers') == 'The Avengers'
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'

check(replace_spaces)