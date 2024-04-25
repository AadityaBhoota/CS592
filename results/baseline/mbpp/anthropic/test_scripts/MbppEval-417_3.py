def group_tuples(input_list):
    result = []
    group_dict = {}

    for tup in input_list:
        first_elem = tup[0]
        if first_elem not in group_dict:
            group_dict[first_elem] = []
        group_dict[first_elem].append(tup)

    for key, value in group_dict.items():
        result.append(tuple([key] + [x[1] for x in value]))

    return result

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)