def count_reverse_pairs(test_list):
    count = 0
    reversed_strings = set()
    
    for string in test_list:
        if string[::-1] in reversed_strings:
            count += 1
            reversed_strings.remove(string[::-1])
        else:
            reversed_strings.add(string)
    
    return str(count)

def check(candidate):
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2

check(count_reverse_pairs)