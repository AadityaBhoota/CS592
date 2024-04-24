def group_tuples(Input):
    result = []
    grouping = {}

    for tup in Input:
        first_element = tup[0]
        if first_element not in grouping:
            grouping[first_element] = []
        grouping[first_element].append(tup[1])

    for key, values in grouping.items():
        result.append((key,) + tuple(values))

    return result

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)