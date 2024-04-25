from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    filtered_strings = []
    for string in strings:
        if string.startswith(prefix):
            filtered_strings.append(string)
    return filtered_strings



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

check(filter_by_prefix)