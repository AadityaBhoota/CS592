def all_prefixes(string: str) -> List[str]:
    result = []
    for i in range(1, len(string)+1):
        result.append(string[:i])
    return result

# Test the function with the example given




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']

check(all_prefixes)