def count_reverse_pairs(test_list):
    """
    Write a function to count the pairs of reverse strings in the given string list.
    Examples:
    count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == '2'
    count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == '1'
    count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == '2'
    """
    reverse_dict = {}
    count = 0
    for item in test_list:
        reverse_item = item[::-1]
        if reverse_item in reverse_dict:
            count += 1
            reverse_dict[reverse_item] += 1
        else:
            reverse_dict[reverse_item] = 1
    return str(count)

def check(candidate):
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2

check(count_reverse_pairs)