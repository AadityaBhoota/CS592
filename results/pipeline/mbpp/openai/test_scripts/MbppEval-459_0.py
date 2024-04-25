import re

def remove_uppercase(str1):
    result = ""
    previous_char_upper = False
    for char in str1:
        if char.isupper() and previous_char_upper:
            pass
        else:
            result += char
            previous_char_upper = char.isupper()
    
    # Remove consecutive uppercase characters
    result = re.sub(r'([A-Z])\1+', r'\1', result)
    
    return result

def check(candidate):
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

check(remove_uppercase)