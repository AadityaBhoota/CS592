def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return count

    start = 0
    while start <= len(string) - len(substring):
        if string[start:start + len(substring)] == substring:
            count += 1
            start += 1
        else:
            start += 1

    return count

# Testing the function with the provided examples
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3



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