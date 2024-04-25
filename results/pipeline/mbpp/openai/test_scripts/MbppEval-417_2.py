from itertools import chain

def group_tuples(Input): 
    grouped_dict = {}
    
    for tup in Input:
        if tup[0] in grouped_dict:
            grouped_dict[tup[0]].append(tup)
        else:
            grouped_dict[tup[0]] = [tup]
    
    return [tuple(chain.from_iterable(grouped_dict_val)) for grouped_dict_val in grouped_dict.values()]

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)