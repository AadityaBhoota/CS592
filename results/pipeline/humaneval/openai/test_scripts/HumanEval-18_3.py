def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases. """
    count = 0
    
    if string == '' or substring == '' or len(substring) > len(string):
        return 0
    
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    
    return count

# Testing the function




# Additional test cases






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