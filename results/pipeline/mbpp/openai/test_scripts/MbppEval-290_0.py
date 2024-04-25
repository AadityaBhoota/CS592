def max_length(list1):
    max_len = 0
    max_list = []

    for sublist in list1:
        sublist_len = len(sublist)
        if sublist_len > max_len:
            max_len = sublist_len
            max_list = sublist

    return max_len, max_list

def check(candidate):
    assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
    assert max_length([[5], [15,20,25]])==(3, [15,20,25])

check(max_length)