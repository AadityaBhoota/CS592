def extract_string(strings, length):
    """
    Write a function to extract specified size of strings from a given list of string values.

    Examples:
    extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
    extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 6) == ['Python']
    extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 9) == ['exercises']
    """
    return [s for s in strings if len(s) == length]

def check(candidate):
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

check(extract_string)