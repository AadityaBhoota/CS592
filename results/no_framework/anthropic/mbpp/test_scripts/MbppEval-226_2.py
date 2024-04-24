def odd_values_string(str):
    """
    Write a python function to remove the characters which have odd index values of a given string.

    Examples:
    odd_values_string('abcdef') == 'ace'
    odd_values_string('python') == 'pto'
    odd_values_string('data') == 'dt'
    """
    return ''.join(str[i] for i in range(len(str)) if i % 2 == 0)

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)