def odd_values_string(str):
    result = ''
    for index in range(len(str)):
        if index % 2 == 0:
            result += str[index]
    return result

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)