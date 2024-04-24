def find_length(string): 
    max_diff = 0
    count_0 = 0
    count_1 = 0
    counts = [(0, 0)]

    for char in string:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1

        counts.append((count_0, count_1))

    for i in range(len(counts) - 1):
        for j in range(i + 1, len(counts)):
            diff = abs(counts[j][0] - counts[i][0])
            max_diff = max(max_diff, diff)

    return max_diff

# Test cases




def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)