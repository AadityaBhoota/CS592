def group_tuples(Input): 
    result = []
    seen = set()
    for tup in Input:
        key = tup[0]
        if key not in seen:
            group = [key]
            for other_tup in Input:
                if other_tup[0] == key:
                    group.extend(other_tup[1:])
            result.append(tuple(group))
            seen.add(key)
    return result

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)