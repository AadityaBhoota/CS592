def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
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