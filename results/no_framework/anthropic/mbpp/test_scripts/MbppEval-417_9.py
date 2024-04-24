def group_tuples(Input):
    result = {}
    for tup in Input:
        if tup[0] not in result:
            result[tup[0]] = []
        result[tup[0]].append(tup[1])
    return [(*key_val,) for key_val in result.items()]

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)