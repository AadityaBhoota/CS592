def odd_values_string(input_str):
    return "".join([input_str[i] for i in range(len(input_str)) if i % 2 == 0])


# Test cases



def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)