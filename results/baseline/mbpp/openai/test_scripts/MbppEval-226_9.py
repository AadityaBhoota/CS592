def odd_values_string(s):
    return s[::2]

# Test the function with examples




def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)