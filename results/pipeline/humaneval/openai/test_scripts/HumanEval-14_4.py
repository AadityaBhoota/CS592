from typing import List

def all_prefixes(string: str) -> List[str]:
    prefixes = []
    
    for i in range(1, len(string)+1):
        prefix = string[:i]
        prefixes.append(prefix)
    
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