def remove_uppercase(s):
    return re.sub(r'[A-Z]', '', s)

# Test cases




def check(candidate):
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

check(remove_uppercase)