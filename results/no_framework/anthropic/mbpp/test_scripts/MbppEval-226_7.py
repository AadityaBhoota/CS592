def odd_values_string(input_str):
    """
    Removes the characters which have odd index values of a given string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The new string with characters at odd indices removed.
    """
    return "".join([char for i, char in enumerate(input_str) if i % 2 == 0])

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
    assert odd_values_string('lambs') == 'lms'

check(odd_values_string)