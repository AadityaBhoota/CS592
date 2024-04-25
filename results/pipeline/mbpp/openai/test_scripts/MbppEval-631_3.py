def replace_spaces(text):
    result = ''
    
    for char in text:
        if char == ' ':
            result += '_'
        else:
            result += char
            
    return result

def check(candidate):
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert replace_spaces('The_Avengers') == 'The Avengers'
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'

check(replace_spaces)