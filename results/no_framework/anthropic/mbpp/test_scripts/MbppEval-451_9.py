import re

def remove_whitespaces(text):
    """
    Write a function to remove all whitespaces from the given string.

    Examples:
    remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    remove_whitespaces(' iOS    Swift ') == 'iOSSwift'
    """
    return re.sub(r'\s+', '', text)

def check(candidate):
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'

check(remove_whitespaces)