def group_tuples(Input): 
    result = []
    temp = []

    for tpl in Input:
        if not temp or tpl[0] == temp[0][0]:
            temp.append(tpl)
        else:
            result.append(tuple(temp[i][1] for i in range(len(temp))))
            temp = [tpl]

    if temp:
        result.append(tuple(temp[i][1] for i in range(len(temp))))

    return result

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)