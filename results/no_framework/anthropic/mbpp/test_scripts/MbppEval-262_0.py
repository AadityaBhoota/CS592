def split_two_parts(list1, L):
    """
    Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.

    Examples:
    split_two_parts([1,1,2,3,4,4,5,1],3) == ([1, 1, 2], [3, 4, 4, 5, 1])
    split_two_parts(['a', 'b', 'c', 'd'],2) == (['a', 'b'], ['c', 'd'])
    split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4) == (['p', 'y', 't', 'h'], ['o', 'n'])
    """
    if L > len(list1):
        raise ValueError("L cannot be greater than the length of the list")
    
    first_part = list1[:L]
    second_part = list1[L:]
    
    return (first_part, second_part)

def check(candidate):
    assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
    assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
    assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])

check(split_two_parts)