def count_distinct_characters(string: str) -> int:
    unique_chars = set()
    for char in string:
        if char.isalpha():
            unique_chars.add(char.lower())
    return len(unique_chars)

# Testing the function





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