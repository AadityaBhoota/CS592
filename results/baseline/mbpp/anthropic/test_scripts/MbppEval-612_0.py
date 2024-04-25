def merge(lst):
    """
    Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.

    Examples:
    merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
    merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
    merge([['x', 'y', 'z'], ['a', 'b', 'c'], ['m', 'n', 'o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'], ['z', 'c', 'o']]
    """
    first = []
    second = []
    for sub_list in lst:
        first.append(sub_list[0])
        second.append(sub_list[1])
    return [first, second]

def check(candidate):
    assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
    assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
    assert merge([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]

check(merge)