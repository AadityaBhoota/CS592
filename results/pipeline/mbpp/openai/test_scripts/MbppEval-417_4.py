def group_tuples(Input): 
    groups = {}

    for tup in Input:
        key = tup[0]

        if key not in groups:
            groups[key] = [tup]
        else:
            groups[key].append(tup)

    return list(groups.values())

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)