def merge(lst):  
    first_list = []
    second_list = []
    
    for sub_list in lst:
        first_list.append(sub_list[0])
        second_list.append(sub_list[1])
    
    return [first_list, second_list]

def check(candidate):
    assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
    assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
    assert merge([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]

check(merge)