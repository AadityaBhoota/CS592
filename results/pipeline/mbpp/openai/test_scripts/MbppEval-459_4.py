import re
def remove_uppercase(str1):
    result = ''
    uppercase_substrings = re.findall(r'[A-Z]+', str1)

    for index, char in enumerate(str1):
        is_upper = False
        for substr in uppercase_substrings:
            if str1[index:index+len(substr)].lower() == substr.lower():
                is_upper = True
                break
        if not is_upper:
            result += char
    return result

def check(candidate):
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

check(remove_uppercase)