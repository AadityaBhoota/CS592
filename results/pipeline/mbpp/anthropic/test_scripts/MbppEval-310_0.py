def string_to_tuple(str1):
    """
    Write a function to convert a given string to a tuple of characters.

    Examples:
    string_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')
    string_to_tuple("item1") == ('i', 't', 'e', 'm', '1')
    string_to_tuple("15.10") == ('1', '5', '.', '1', '0')
    """
    return tuple(char for char in str1)

def check(candidate):
    assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
    assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')

check(string_to_tuple)