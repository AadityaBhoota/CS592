def count_reverse_pairs(test_list):
    reverse_pairs_count = 0
    
    for word in test_list:
        reverse_word = word[::-1]
        if reverse_word != word and reverse_word in test_list:
            reverse_pairs_count += 1
    
    return str(reverse_pairs_count)

def check(candidate):
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2

check(count_reverse_pairs)