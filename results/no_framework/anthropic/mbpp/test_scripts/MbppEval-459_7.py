import re

def remove_uppercase(str1):
    """
    Write a function to remove uppercase substrings from a given string.

    Examples:
    remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'
    """
    return re.sub(r'[A-Z]+', '', str1)

def check(candidate):
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

check(remove_uppercase)