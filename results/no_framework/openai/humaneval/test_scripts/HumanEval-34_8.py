def unique(l: list):
    unique_list = list(set(l))  # Convert the list to a set to remove duplicates, then convert back to list
    unique_list.sort()  # Sort the list in ascending order
    return unique_list

# Test the function with the example from the docstring




METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


check(unique)