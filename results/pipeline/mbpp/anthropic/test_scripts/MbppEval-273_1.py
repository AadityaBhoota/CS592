def substract_elements(test_tup1, test_tup2):
    '''
    Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.

    Examples:
    substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
    substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
    substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)
    '''
def subtract_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Input tuples must have the same length."
    
    result = []
    for i in range(len(test_tup1)):
        result.append(test_tup1[i] - test_tup2[i])
    
    return tuple(result)

def check(candidate):
    assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
    assert substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
    assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)

check(substract_elements)