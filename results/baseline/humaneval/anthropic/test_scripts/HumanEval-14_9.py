from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string.
        
    Returns:
        List[str]: A list of all prefixes from shortest to longest.
    
    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']

check(all_prefixes)