def max_length(list1):
    max_length = 0
    max_list = []

    for inner_list in list1:
        if len(inner_list) > max_length:
            max_length = len(inner_list)
            max_list = inner_list

    return (max_length, max_list)

def check(candidate):
    assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
    assert max_length([[5], [15,20,25]])==(3, [15,20,25])

check(max_length)