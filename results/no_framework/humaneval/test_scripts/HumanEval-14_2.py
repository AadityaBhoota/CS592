from typing import List

def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(1, len(string)+1)]
    return prefixes

# Test the function




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']

check(all_prefixes)