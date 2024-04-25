def odd_values_string(str):
    result = ""
    for i in range(1, len(str), 2):
        result += str[i]
    return result

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)