def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Create a set of characters in the string to get distinct characters
    distinct_chars = set(string)
    
    # Return the count of distinct characters
    return len(distinct_chars)

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