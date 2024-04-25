def group_tuples(input_list):
    grouped = {}
    
    for tup in input_list:
        first_element = tup[0]
        if first_element not in grouped:
            grouped[first_element] = []
        grouped[first_element].append(tup)
    
    return [tuple(group) for group in grouped.values()]

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)