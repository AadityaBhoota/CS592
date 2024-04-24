def count_distinct_characters(string: str) -> int:
    string = string.lower()  # convert the string to lowercase
    distinct_characters = set(string)  # find unique characters using set
    return len(distinct_characters)

# Test cases





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