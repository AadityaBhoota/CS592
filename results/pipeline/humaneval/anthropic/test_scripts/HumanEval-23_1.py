def strlen(string: str) -> int:
    length = 0
    for _ in string:
        length += 1
    return length



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9

check(strlen)