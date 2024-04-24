def group_tuples(input_list):
    # Create a dictionary to group the tuples
    grouped = {}

    # Iterate through the input list
    for tup in input_list:
        # Get the first element of the tuple
        first = tup[0]

        # If the first element is not in the dictionary, add it
        if first not in grouped:
            grouped[first] = []

        # Add the tuple to the list for the corresponding first element
        grouped[first].append(tup)

    # Convert the dictionary back to a list of tuples
    result = [tuple(v) for v in grouped.values()]
    return result

def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)