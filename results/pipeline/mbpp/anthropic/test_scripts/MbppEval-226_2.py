def odd_values_string(str):
    result = ""
    for i, char in enumerate(str):
        if i % 2 == 0:
            result += char
    return result

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)