def all_prefixes(string: str) -> List[str]:
    prefixes = []
    
    for char in string:
        prefixes.append(char)
        
    for i in range(1, len(string)):
        prefixes.append(string[:i+1])



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']

check(all_prefixes)