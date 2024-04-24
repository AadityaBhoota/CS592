def group_tuples(input_tuples):
    result = {}
    for tup in input_tuples:
        first_element = tup[0]
        if first_element in result:
            result[first_element].append(tup[1])
        else:
            result[first_element] = [tup[1]]
    return [(*key_value,) for key_value in result.items()]

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)