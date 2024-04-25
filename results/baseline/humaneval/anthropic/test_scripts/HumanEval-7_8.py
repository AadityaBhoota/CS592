from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.
    
    Args:
    strings (List[str]): The list of strings to filter.
    substring (str): The substring to search for.
    
    Returns:
    List[str]: A new list containing only the strings that contain the given substring.
    """
    return [s for s in strings if substring in s]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
    assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']
    assert candidate(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune']

check(filter_by_substring)