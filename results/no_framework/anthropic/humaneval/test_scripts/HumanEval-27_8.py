def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with the case of each character flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    result = ""
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)