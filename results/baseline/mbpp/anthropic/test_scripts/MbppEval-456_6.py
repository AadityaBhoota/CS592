def reverse_string_list(string_list):
    """
    Reverses each string in the given list of strings.

    Args:
        string_list (list): A list of string values.

    Returns:
        list: A new list with each string reversed.
    """
    reversed_strings = []
    for string in string_list:
        reversed_strings.append(string[::-1])
    return reversed_strings

def check(candidate):
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']

check(reverse_string_list)