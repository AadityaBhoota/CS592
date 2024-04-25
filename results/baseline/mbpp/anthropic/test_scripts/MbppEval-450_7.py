def extract_string(str_list, length):
    """
    Write a function to extract specified size of strings from a given list of string values.

    Args:
        str_list (list): A list of string values.
        length (int): The desired length of the strings to be extracted.

    Returns:
        list: A list of strings with the specified length.
    """
    return [s for s in str_list if len(s) == length]

def check(candidate):
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

check(extract_string)