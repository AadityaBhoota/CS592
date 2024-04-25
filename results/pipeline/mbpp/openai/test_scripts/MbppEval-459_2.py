def remove_uppercase(str1):
    result = ''
    for char in str1:
        if not char.isupper():
            result += char
    return result

def check(candidate):
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

check(remove_uppercase)