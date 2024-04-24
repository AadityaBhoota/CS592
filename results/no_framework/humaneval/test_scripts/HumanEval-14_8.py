from typing import List

def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i+1] for i in range(len(string))]
    return prefixes

# Testing the function with the example provided
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']

check(all_prefixes)