def find_length(string):
    max_diff = 0
    diff = 0

    for char in string:
        if char == '0':
            diff += 1
        else:
            diff -= 1

        diff = max(0, diff)
        max_diff = max(max_diff, diff)

    return max_diff

# Testing the function with the given examples




def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)