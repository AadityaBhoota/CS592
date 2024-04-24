def strlen(string: str) -> int:
    return len(string)

# Test cases
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9

check(strlen)