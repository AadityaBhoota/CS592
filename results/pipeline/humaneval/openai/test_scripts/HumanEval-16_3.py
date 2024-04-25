def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = set()

    # Convert the input string to lowercase
    lowercase_string = string.lower()
    
    # Iterate through each character in the lowercase string
    for char in lowercase_string:
        # Check if the character is a letter and add it to the set
        if char.isalpha():
            distinct_chars.add(char)

    # Return the length of the set containing unique characters
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