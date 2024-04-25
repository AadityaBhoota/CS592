def reverse_string_list(string_list):
    """
    Write a function to reverse each string in a given list of string values.

    Examples:
    reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    reverse_string_list(['john','amal','joel','george']) == ['nhoj','lama','leoj','egroeg']
    reverse_string_list(['jack','john','mary']) == ['kcaj','nhoj','yram']
    """
    reversed_list = []
    for string in string_list:
        reversed_list.append(string[::-1])
    return reversed_list

def check(candidate):
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']

check(reverse_string_list)