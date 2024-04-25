def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to make the comparison case-insensitive
    string = string.lower()
    
    # Use a set to store the distinct characters
    distinct_chars = set(string)
    
    # Return the length of the set, which represents the count of distinct characters
    return len(distinct_chars)

# Testing the function
if __name__ == "__main__":
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