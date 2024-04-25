from collections import Counter

def count_Occurrence(tup, lst):
    elem_counts = Counter(tup)
    total_count = 0

    for ele in lst:
        total_count += elem_counts[ele]

    return total_count

def check(candidate):
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2

check(count_Occurrence)