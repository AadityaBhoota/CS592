def group_tuples(input_list):
    result = []
    grouped_tuples = {}

    for tup in input_list:
        first_elem = tup[0]
        if first_elem in grouped_tuples:
            grouped_tuples[first_elem].append(tup[1])
        else:
            grouped_tuples[first_elem] = [tup[1]]

    for key, values in grouped_tuples.items():
        result.append((key,) + tuple(values))

    return result

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)