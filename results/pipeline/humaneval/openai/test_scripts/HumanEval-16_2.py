def count_distinct_characters(string: str) -> int:
    distinct_chars = set()

    for char in string:
        char_lower = char.lower()
        distinct_chars.add(char_lower)

    return len(distinct_chars)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('abcde') == 5
    assert candidate('abcde' + 'cade' + 'CADE') == 5
    assert candidate('aaaaAAAAaaaa') == 1
    assert candidate('Jerry jERRY JeRRRY') == 5

check(count_distinct_characters)