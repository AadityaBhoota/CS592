def remove_whitespaces(text1):
    return re.sub(r'\s+', '', text1)

# Testing the function with the given examples




def check(candidate):
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'

check(remove_whitespaces)