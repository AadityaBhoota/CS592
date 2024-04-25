def group_tuples(input_list):
    """
    Find common first element in the given list of tuples and group them together.

    Args:
        input_list (list): A list of tuples.

    Returns:
        list: A list of tuples where the first elements are common.
    """
    result = {}

    for item in input_list:
        first_element = item[0]
        if first_element in result:
            result[first_element].append(item[1])
        else:
            result[first_element] = [item[1]]

    return [(*key_value,) for key_value in result.items()]

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)