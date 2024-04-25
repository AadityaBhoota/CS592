def count_reverse_pairs(test_list):
    count = 0
    
    for string in test_list:
        reverse_string = string[::-1]
        if reverse_string in test_list:
            count += 1

    return str(count)

def check(candidate):
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2

check(count_reverse_pairs)