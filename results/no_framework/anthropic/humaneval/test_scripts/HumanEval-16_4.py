def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) it consists of.
    
    Args:
    string (str): The input string.
    
    Returns:
    int: The number of distinct characters in the string.
    """
    # Convert the string to lowercase to make the comparison case-insensitive
    string = string.lower()
    
    # Convert the string to a set to remove duplicates
    distinct_chars = set(string)
    
    # Return the length of the set, which represents the number of distinct characters
    return len(distinct_chars)


# Example usage





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