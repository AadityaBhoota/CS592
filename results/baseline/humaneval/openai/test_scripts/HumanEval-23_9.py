def strlen(string: str) -> int:
    """Return length of given string"""
    return len(string)

# Testing the function
if __name__ == "__main__":
    import doctest
    doctest.testmod()



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9

check(strlen)