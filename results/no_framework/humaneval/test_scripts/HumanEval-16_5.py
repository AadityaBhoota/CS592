def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ensure case insensitivity
    string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Add the character to the set
        unique_chars.add(char)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4



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