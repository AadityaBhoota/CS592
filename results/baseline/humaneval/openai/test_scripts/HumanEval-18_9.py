def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0

    count = 0
    start = 0
    while start <= len(string) - len(substring):
        if string[start:start+len(substring)] == substring:
            count += 1
        start += 1
    return count

# Test cases






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