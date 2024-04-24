import re

def remove_uppercase(str1):
    return re.sub(r'[A-Z]', '', str1)

# Test the function with the provided examples




def check(candidate):
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

check(remove_uppercase)