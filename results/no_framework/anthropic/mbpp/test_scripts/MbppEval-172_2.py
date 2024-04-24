def count_occurance(s):
    """
    Write a function to count the number of occurrences of the string 'std' in a given string.

    Examples:
    count_occurance("letstdlenstdporstd") == 3
    count_occurance("truststdsolensporsd") == 1
    count_occurance("makestdsostdworthit") == 2
    """
    return s.count("std")

def check(candidate):
    assert count_occurance("letstdlenstdporstd") == 3
    assert count_occurance("truststdsolensporsd") == 1
    assert count_occurance("makestdsostdworthit") == 2
    assert count_occurance("stds") == 1
    assert count_occurance("") == 0

check(count_occurance)