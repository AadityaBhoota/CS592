def group_tuples(Input): 
    output = []
    for tup in Input:
        found = False
        for grp in output:
            if tup[0] in grp:
                grp += (tup[1],)
                found = True
                break
        if not found:
            output.append(list(tup))
    return output

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)