def group_tuples(Input): 
    groups = {}
    
    for tup in Input:
        first_element = tup[0]
        if first_element in groups:
            if tup not in groups[first_element]:
                groups[first_element].append(tup)
        else:
            groups[first_element] = [tup]
    
    return [val for val in groups.values()]

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)