def group_tuples(Input):
    output = []
    temp_dict = {}
    
    for tpl in Input:
        key = tpl[0]
        if key in temp_dict:
            temp_dict[key].append(tpl[1])
        else:
            temp_dict[key] = [tpl[1]]
    
    for key, values in temp_dict.items():
        output.append((key, *values))
    
    return output

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)