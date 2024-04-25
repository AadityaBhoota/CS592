def split_two_parts(list1, L):
    first_part = []
    second_part = []
    for i, item in enumerate(list1):
        if i < L:
            first_part.append(item)
        else:
            second_part.append(item)
    return (first_part, second_part)

def check(candidate):
    assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
    assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
    assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])

check(split_two_parts)