def group_tuples(Input): 
    common_first = {}
    for t in Input:
        if t[0] in common_first:
            common_first[t[0]].append(t[1])
        else:
            common_first[t[0]] = [t[1]]
    
    result = []
    for key, values in common_first.items():
        result.append((key,) + tuple(values))
    
    return result

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)