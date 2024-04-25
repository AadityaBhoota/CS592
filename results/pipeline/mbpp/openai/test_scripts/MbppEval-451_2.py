import re

def remove_whitespaces(text1):
    whitespace_pattern = r'\s+'
    whitespaces = re.findall(whitespace_pattern, text1)
    for space in whitespaces:
        text1 = text1.replace(space, '')
    return text1

def check(candidate):
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'

check(remove_whitespaces)