def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Count overlaping cases.
    
    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.
    
    Returns:
        int: The number of times the substring is found in the original string.
    """
    if not string or not substring:
        return 0
    
    count = 0
    start = 0
    
    while start < len(string):
        index = string.find(substring, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    
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