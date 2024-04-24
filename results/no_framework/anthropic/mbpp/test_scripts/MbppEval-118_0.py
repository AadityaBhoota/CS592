def string_to_list(string):
    """
    Write a function to convert a string to a list of strings split on the space character.

    Examples:
    string_to_list("python programming") == ['python', 'programming']
    string_to_list("lists tuples strings") == ['lists', 'tuples', 'strings']
    string_to_list("write a program") == ['write', 'a', 'program']
    """
    return string.split()

def check(candidate):
    assert string_to_list("python programming")==['python','programming']
    assert string_to_list("lists tuples strings")==['lists','tuples','strings']
    assert string_to_list("write a program")==['write','a','program']

check(string_to_list)