def count_first_elements(test_tup):
    index = test_tup.index((4, 6))
    return index

# Test cases




def check(candidate):
    assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
    assert count_first_elements((2, 9, (5, 7), 11) ) == 2
    assert count_first_elements((11, 15, 5, 8, (2, 3), 8) ) == 4

check(count_first_elements)