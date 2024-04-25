def concatenate_tuple(test_tup, delimiter='-'):
    """
    Write a function to concatenate each element of tuple by the delimiter.

    Args:
        test_tup (tuple): The input tuple to be concatenated.
        delimiter (str, optional): The delimiter to be used for concatenation. Defaults to '-'.

    Returns:
        str: The concatenated string.
    """
    return delimiter.join(map(str, test_tup))

def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

check(concatenate_tuple)