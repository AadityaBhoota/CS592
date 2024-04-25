def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases."""
    
    # Handle corner case when input string is empty
    if not string:
        return 0
    
    count = 0
    substr_len = len(substring)
    
    # Count the number of occurrences of the substring in the string
    for i in range(len(string) - substr_len + 1):
        if string[i:i+substr_len] == substring:
            count += 1
            
    return count



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('', 'x') == 0
    assert candidate('xyxyxyx', 'x') == 4
    assert candidate('cacacacac', 'cac') == 4
    assert candidate('john doe', 'john') == 1

check(how_many_times)