import re

def remove_whitespaces(text1):
    regex_pattern = r'\s+'
    text_without_spaces = re.sub(regex_pattern, '', text1)
    return text_without_spaces

def check(candidate):
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'

check(remove_whitespaces)