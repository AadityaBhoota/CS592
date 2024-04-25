from typing import List

def all_prefixes(string: str) -> List[str]:
    prefixes = []
    
    for i in range(len(string)):
        prefix = string[:i+1]
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