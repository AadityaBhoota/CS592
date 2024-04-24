def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return count

    start = 0
    while True:
        index = string.find(substring, start)
        if index == -1:
            break

        count += 1
        start = index + 1

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