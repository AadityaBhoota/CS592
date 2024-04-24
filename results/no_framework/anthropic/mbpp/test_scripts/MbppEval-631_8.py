def replace_spaces(text):
    """
    Write a function to replace whitespaces with an underscore and vice versa in a given string.

    Examples:
    replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    replace_spaces('The Avengers') == 'The_Avengers'
    replace_spaces('Fast and Furious') == 'Fast_and_Furious'
    """
    return text.replace(' ', '_').replace('_', ' ')

def check(candidate):
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert replace_spaces('The_Avengers') == 'The Avengers'
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'

check(replace_spaces)