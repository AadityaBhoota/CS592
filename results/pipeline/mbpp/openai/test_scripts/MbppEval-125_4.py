def find_length(string):
    max_diff = 0
    count = 0

    for char in string:
        if char == '0':
            count -= 1
        else:
            count += 1

        max_diff = max(max_diff, abs(count))

    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)