def group_tuples(Input):
    grouped_dict = {}
    
    for tup in Input:
        first_element = tup[0]
        
        if first_element in grouped_dict:
            grouped_dict[first_element].append(tup)
        else:
            grouped_dict[first_element] = [tup]
           
    return list(grouped_dict.values())

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)