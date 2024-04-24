def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be flipped.
        
    Returns:
        str: The flipped string.
        
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)