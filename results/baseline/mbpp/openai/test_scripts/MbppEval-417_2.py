def group_tuples(tuples):
    grouped = {}
    for tpl in tuples:
        key = tpl[0]
        if key in grouped:
            grouped[key].append(tpl[1])
        else:
            grouped[key] = [key, tpl[1]]

    res = [tuple(val) for key, val in grouped.items()]
    return res

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)