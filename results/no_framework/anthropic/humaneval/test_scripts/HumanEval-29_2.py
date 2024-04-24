from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.
    
    Args:
        strings (List[str]): The input list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.
    
    Returns:
        List[str]: A new list of strings that start with the given prefix.
    """
    return [s for s in strings if s.startswith(prefix)]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

check(filter_by_prefix)