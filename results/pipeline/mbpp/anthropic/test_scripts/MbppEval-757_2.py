def count_reverse_pairs(test_list):
    reverse_dict = {}
    count = 0
    for s in test_list:
        reverse_s = s[::-1]
        if reverse_s in reverse_dict:
            count += 1
            reverse_dict[reverse_s] += 1
        else:
            reverse_dict[reverse_s] = 1
    return str(count)

def check(candidate):
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2

check(count_reverse_pairs)