def group_tuples(Input):
    result = []
    group_dict = {}
    
    for item in Input:
        key = item[0]
        if key not in group_dict:
            group_dict[key] = [item]
        else:
            group_dict[key].append(item)
            
    for key in group_dict:
        if len(group_dict[key]) > 1:
            new_tuple = tuple([key] + sorted(set([element for tup in group_dict[key] for element in tup[1:]])))
            result.append(new_tuple)
        else:
            result.append(tuple(group_dict[key][0]))
    
    return result

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)