def replace_spaces(text):
    return ''.join(['_' if c == ' ' else ' ' if c == '_' else c for c in text])

# Test the function with the given examples




def check(candidate):
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert replace_spaces('The_Avengers') == 'The Avengers'
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'

check(replace_spaces)