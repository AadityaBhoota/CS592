def extract_string(strings, length):
    """
    Extracts strings of the specified length from a list of strings.

    Args:
        strings (list): A list of string values.
        length (int): The desired length of the extracted strings.

    Returns:
        list: A list of strings of the specified length.
    """
    return [s for s in strings if len(s) == length]

def check(candidate):
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

check(extract_string)