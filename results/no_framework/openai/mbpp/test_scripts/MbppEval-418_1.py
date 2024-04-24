def Find_Max(lst):
    max_length = 0
    max_element = None

    for element in lst:
        if len(element) > max_length:
            max_length = len(element)
            max_element = element

    return max_element

# Test the function with examples




def check(candidate):
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]

check(Find_Max)