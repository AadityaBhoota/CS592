def Find_Max(lst):
    """
    Write a python function to find the element of a list having maximum length.

    Examples:
    Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]
    """
    return max(lst, key=lambda x: len(x))

def check(candidate):
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]

check(Find_Max)