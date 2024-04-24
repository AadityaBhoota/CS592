def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return count
    if len(substring) > len(string):
        return count
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3



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